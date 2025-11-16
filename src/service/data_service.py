from dto import NewCheckDTO
from src.repository.data_repo import DataRepo


class DataService:
    def __init__(self, repository: DataRepo):
        self._repository = repository

    def save_data(self, data: NewCheckDTO) -> None:
        self._repository.save(data)

    def get_data(self) -> NewCheckDTO:
        return self._repository.get()
    
    def clear_data(self) -> None:
        self._repository.clear()