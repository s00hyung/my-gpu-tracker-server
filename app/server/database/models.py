from pydantic import BaseModel, Field
from typing import List


class Price(BaseModel):
    value: int = Field(...)
    currency: str = Field(...)
    date: str = Field(...)


class Gpu(BaseModel):
    id: str = Field(..., alias="_id")
    name: str = Field(...)
    description: str = Field(...)
    manufacturer: str = Field(...)
    last_updated: str = Field(...)
    price_data: List[Price] = Field(...)
