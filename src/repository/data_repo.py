from dto import ProductDTOandMenuDTO


class DataRepo:
    def __init__(self):
        self._data = None

    def save(self, data: ProductDTOandMenuDTO) -> None:
        self._data = data

    def get(self) -> ProductDTOandMenuDTO:
        return self._data