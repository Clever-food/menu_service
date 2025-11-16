from typing import List
import pydantic
    
class MenuDTO(pydantic.BaseModel):
    id: int
    dish_class: int
    dish_name: str
    is_portionable: bool | None = None
    weight_volume: int | None = None
    price: int | None = None
    
class DetectedDish(pydantic.BaseModel):
    id: int
    dish_class: int
    amount: float

class ChequeDTO(pydantic.BaseModel):
    detected_dish: List[DetectedDish]

class NewCheckDTO(pydantic.BaseModel):
    id: int
    dish_name: str
    amount: float
    price: int