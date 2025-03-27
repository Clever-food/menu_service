from dto import MenuDTO
from src.models.menu_model import MenuModel
import peewee
class MenuRepo:
    class EntityDoesNotExist(Exception):
        message = f"Entity does not exist in table"
        def __init__(self, _model, *args) -> None:
            super().__init__(*args)
            self.model = _model

    class EntityNoMinimumLength(Exception):
        message = "The length of the 'name' field must be at least 3 characters"
        def __init__(self, _model, *args) -> None:
            super().__init__(*args)
            self.model = _model

    def __init__(
            self, 
            menu_model: MenuModel, 
            menu_dto: MenuDTO
        ) -> None:

        self.menu_model: MenuModel = menu_model
        self.menu_dto: MenuDTO = menu_dto

    def get_menu_item(
            self,
            menu_id: int
    ):
        try:
            menu_item = self.menu_model.get(
                menu_id=menu_id
            )
            return MenuDTO(
                menu_id=menu_item.menu_id,
                name=menu_item.name,
                price=menu_item.price,
                volume=menu_item.volume
            )
        except peewee.DoesNotExist:
            raise self.EntityDoesNotExist(self.menu_model)
    
    def add_menu_item(
        self, 
        name: str, 
        price: int,
        volume: int,
    ):
        if len(name) < 3:
            raise self.EntityNoMinimumLength(self.menu_model)
        return self.menu_model.insert(
            name=name,
            price=price,
            volume=volume,
        ).execute()
