from typing import List
import peewee

from dto import MenuDTO
from src.models.menu_model import MenuModel


class MenuRepo:
    class EntityDoesNotExist(Exception):
        message = "Entity does not exist in table"

        def __init__(self, _model, *args) -> None:
            super().__init__(*args)
            self.model = _model

    class EntityNoMinimumLength(Exception):
        message = "The length of the 'dish_name' field must be at least 3 characters"

        def __init__(self, _model, *args) -> None:
            super().__init__(*args)
            self.model = _model

    def __init__(self, menu_model: MenuModel) -> None:
        self.menu_model = menu_model

    def get_menu_item(self, id: int) -> MenuDTO:
        try:
            item = self.menu_model.get(self.menu_model.id == id)
            return MenuDTO(
                id=item.id,
                dish_class=item.dish_class,
                dish_name=item.dish_name,
                is_portionable=item.is_portionable,
                weight_volume=item.weight_volume,
                price=item.price,
            )
        except peewee.DoesNotExist:
            raise self.EntityDoesNotExist(self.menu_model)

    def add_menu_item(
        self,
        dish_class: int,
        dish_name: str,
        is_portionable: bool | None = None,
        weight_volume: int | None = None,
        price: int | None = None,
    ) -> int:
        if len(dish_name) < 3:
            raise self.EntityNoMinimumLength(self.menu_model)

        new_id = (
            self.menu_model.insert(
                dish_class=dish_class,
                dish_name=dish_name,
                is_portionable=is_portionable,
                weight_volume=weight_volume,
                price=price,
            ).execute()
        )

        return new_id

    def delete_menu_item(self, id: int) -> int:
        deleted = (
            self.menu_model.delete()
            .where(self.menu_model.id == id)
            .execute()
        )
        if deleted == 0:
            raise self.EntityDoesNotExist(self.menu_model)

        return deleted


    def get_all_menu_items(self) -> List[MenuDTO]:
        query = self.menu_model.select()

        return [
            MenuDTO(
                id=item.id,
                dish_class=item.dish_class,
                dish_name=item.dish_name,
                is_portionable=item.is_portionable,
                weight_volume=item.weight_volume,
                price=item.price,
            )
            for item in query
        ]
