from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True

class DeleteResponse(BaseModel):
    status: str = "success"
    message: str = "Item deletado com sucesso"
    id: int

    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "message": "Item deletado com sucesso",
                "id": 1
            }
        }