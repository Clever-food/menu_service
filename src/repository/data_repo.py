from dto import NewCheckDTO


class DataRepo:
    def __init__(self):
        self._data = None

    def save(self, data: NewCheckDTO) -> None:
        self._data = data

    def get(self) -> NewCheckDTO:
        return self._data
    
    def clear(self):
        self.save(None)