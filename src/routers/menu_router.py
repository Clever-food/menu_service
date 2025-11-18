import asyncio
from typing import List
from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from src.service.admin_service import AdminService
from src.service.data_service import DataService
from src.service.connection_service import ConnectionService
from src.app.http_exceptions import EntityDoesNotExistError, EntityNoMinimumLength
from depends import get_code, get_data_storage, get_menu_service, get_websocket_manager
from dto import ChequeDTO, NewCheckDTO
from src.service.menu_processing_service import MenuProcessingService

menu_router = APIRouter(
    prefix="/menu",
    tags=["menu"]
)

@menu_router.get("/get-menu-item")
def get_menu_item(
    menu_id: int,
    menu_processing_service: MenuProcessingService = Depends(get_menu_service)
):
    try:
        return menu_processing_service.get_menu_item(menu_id)
    except menu_processing_service.EntityDoesNotExist as e:
        raise EntityDoesNotExistError(e.model)


@menu_router.post("/add-menu-item")
def add_menu_item(
    dish_class: int,
    dish_name: str,
    is_portionable: bool | None = None,
    weight_volume: int | None = None,
    price: int | None = None,
    menu_processing_service: MenuProcessingService = Depends(get_menu_service),
):
    try:
        return menu_processing_service.add_menu_item(
            dish_class=dish_class,
            dish_name=dish_name,
            is_portionable=is_portionable,
            weight_volume=weight_volume,
            price=price,
        )
    except menu_processing_service.EntityNoMinimumLength as e:
        raise EntityNoMinimumLength(e.model)


@menu_router.delete("/delete-menu-item")
def delete_menu_item(
    menu_id: int,
    menu_processing_service: MenuProcessingService = Depends(get_menu_service)
):
    try:
        return menu_processing_service.delete_menu_item(menu_id)
    except menu_processing_service.EntityDoesNotExist as e:
        raise EntityDoesNotExistError(e.model)


@menu_router.get("/get-all-menu")
def get_all_menu(
    menu_processing_service: MenuProcessingService = Depends(get_menu_service)
):
    try:
        items = menu_processing_service.get_all_menu_items()
        if not items:
            return JSONResponse(
                status_code=200,
                content={"detail": "Menu is empty", "items": []}
            )
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Возникла ошибка: {e}")


@menu_router.post("/get-cheque-item")
def get_cheque_item(
    cheque: ChequeDTO,
    menu_processing_service: MenuProcessingService = Depends(get_menu_service),
    data_storage: DataService = Depends(get_data_storage)
):
    try:
        res: List[NewCheckDTO] | str = menu_processing_service.get_cheque_item(cheque)
        data_storage.save_data(res)
        return res
    except menu_processing_service.EntityDoesNotExist as e:
        if data_storage is not None:
            data_storage.save_data([])
        raise EntityDoesNotExistError(e.model)


@menu_router.get("/get-saved-data")
def get_saved_data(data_storage: DataService = Depends(get_data_storage)):
    saved_data = data_storage.get_data()
    if saved_data is None:
        raise HTTPException(status_code=404, detail="No data saved yet")
    return {"saved_data": saved_data}


@menu_router.websocket("/get-saved-data-ws")
async def get_saved_data_websocket(
    websocket: WebSocket,
    connection_service: ConnectionService = Depends(get_websocket_manager),
    data_storage: DataService = Depends(get_data_storage)
):
    await connection_service.connect(websocket)
    last_sent_data = None
    try:
        while True:
            saved_data = data_storage.get_data()
            if saved_data != last_sent_data:
                if not saved_data:
                    await connection_service.broadcast({"error": "No data saved yet"})
                else:
                    await connection_service.broadcast(saved_data)
                last_sent_data = saved_data
            await asyncio.sleep(0.5)
    except WebSocketDisconnect:
        connection_service.disconnect(websocket)



@menu_router.get("/check-code")
def check_code(
    code: int,
    admin_service: AdminService = Depends(get_code)
):
    return admin_service.check_code(code)

@menu_router.delete("/clear-saved-data")
async def clear_saved_data(
    data_storage: DataService = Depends(get_data_storage),
    connection_service: ConnectionService = Depends(get_websocket_manager)
):
    try:
        data_storage.save_data([])
        await connection_service.broadcast({"error": "Data cleared"})
        return {"detail": "Saved data cleared"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Возникла ошибка: {e}")
