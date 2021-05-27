from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Price(BaseModel):
    date: str = None
    value: int = Field(...)
    currency: str = Field(...)
    last_updated: datetime = None

    class Config:
        schema_extra = {
            "example": {"value": 1500000, "currency": "KRW"},
        }


class Gpu(BaseModel):
    id: str = Field(..., alias="_id")
    name: str = Field(...)
    description: str = Field(...)
    manufacturer: str = Field(...)
    info_last_updated: datetime = None
    price_last_updated: datetime = None
    price_data: Optional[Price] = Field(default_factory=list)

    class Config:
        schema_extra = {
            f"example": {
                "_id": "rtx3090",
                "name": "NVDIA RTX 3090",
                "description": "Powerful One.",
                "manufacturer": "NVDIA",
            }
        }


class GpuUpdate(BaseModel):
    id: str = Field(..., alias="_id")
    name: str = None
    description: str = None
    manufacturer: str = None

    class Config:
        schema_extra = {
            f"example": {
                "_id": "rtx3090",
                "name": "NVDIA RTX 3090",
                "description": "Powerful One.",
                "manufacturer": "NVDIA",
            }
        }


class PriceUpdate(BaseModel):
    date: str = Field(...)
    value: int = Field(...)
    currency: str = None

    class Config:
        schema_extra = {
            "example": {"date": "2021-05-21", "value": 1500000},
        }
