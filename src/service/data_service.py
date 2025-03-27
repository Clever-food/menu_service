from dto import ProductDTOandMenuDTO
from src.repository.data_repo import DataRepo


class DataService:
    def __init__(self, repository: DataRepo):
        self._repository = repository

    def save_data(self, data: ProductDTOandMenuDTO) -> None:
        self._repository.save(data)

    def get_data(self) -> ProductDTOandMenuDTO:
        return self._repository.get()