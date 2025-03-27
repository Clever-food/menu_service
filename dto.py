from typing import List
import pydantic
from pydantic_settings import BaseSettings, SettingsConfigDict

class AdminSettings(BaseSettings):
    ADMIN_CODE: int
    ADMIN_TOKEN: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
    
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