from typing import List
from dto import ChequeDTO, MenuDTO, NewCheckDTO
from src.repository.menu_repo import MenuRepo

class MenuProcessingService:
    class EntityDoesNotExist(Exception):
        def __init__(self, _model, *args) -> None:
            super().__init__(*args)
            self.model = _model

    class EntityNoMinimumLength(Exception):
        def __init__(self, _model, *args) -> None:
            super().__init__(*args)
            self.model = _model

    def __init__(self, menu_repo: MenuRepo):
        self.menu_repo = menu_repo

    def get_menu_item(self, menu_id: int) -> MenuDTO:
        try:
            return self.menu_repo.get_menu_item(menu_id)
        except self.menu_repo.EntityDoesNotExist as e:
            raise self.EntityDoesNotExist(e.model)

    def add_menu_item(
        self,
        dish_class: int,
        dish_name: str,
        is_portionable: bool | None = None,
        weight_volume: int | None = None,
        price: int | None = None,
    ) -> int:
        try:
            return self.menu_repo.add_menu_item(
                dish_class=dish_class,
                dish_name=dish_name,
                is_portionable=is_portionable,
                weight_volume=weight_volume,
                price=price,
            )
        except self.menu_repo.EntityNoMinimumLength as e:
            raise self.EntityNoMinimumLength(e.model)

    def delete_menu_item(self, menu_id: int) -> int:
        try:
            return self.menu_repo.delete_menu_item(menu_id)
        except self.menu_repo.EntityDoesNotExist as e:
            raise self.EntityDoesNotExist(e.model)

    def get_all_menu_items(self) -> List[MenuDTO]:
        return self.menu_repo.get_all_menu_items()

    def get_cheque_item(self, cheque: ChequeDTO) -> List[NewCheckDTO] | str:
        enriched_products: List[NewCheckDTO] = []

        for item in cheque.detected_dish:
            try:
                menu_item = self.menu_repo.get_menu_item(item.id)
                enriched_products.append(
                    NewCheckDTO(
                        id = menu_item.id,
                        dish_name = menu_item.dish_name,
                        amount = item.amount,
                        price = menu_item.price,
                    ).dict()
                )
            except self.menu_repo.EntityDoesNotExist:
                continue

        if not enriched_products:
            return "0"

        return enriched_products
