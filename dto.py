from typing import List
import pydantic
    
class MenuDTO(pydantic.BaseModel):
    name: str
    price: int
    volume: int
    
class MenuDTOwithID(pydantic.BaseModel):
    menu_id: int
    name: str
    price: int
    volume: int
class ProductDTO(pydantic.BaseModel):
    real_id: int
    menu_item_id: int
    amount: int

class ChequeDTO(pydantic.BaseModel):
    task_id: int
    product_list: List[ProductDTO]

class ProductDTOandMenuDTO(ProductDTO, MenuDTO):
    pass