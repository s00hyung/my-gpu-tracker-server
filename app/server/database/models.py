from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Price(BaseModel):
    date: str = Field(..., alias="_id")
    value: int = Field(...)
    currency: str = Field(...)

    class Config:
        schema_extra = {
            "example": {"_id": "2021-01-01", "value": 1500000, "currency": "KRW"}
        }


class Gpu(BaseModel):
    id: str = Field(..., alias="_id")
    name: str = Field(...)
    description: str = Field(...)
    manufacturer: str = Field(...)
    last_updated: datetime = Field(...)
    price_data: Optional[Price] = Field(default_factory=list)

    class Config:
        schema_extra = {
            "example": {
                "_id": "rtx3090",
                "name": "NVDIA RTX 3090",
                "description": "Powerful One.",
                "manufacturer": "NVDIA",
                "last_updated": "2021-01-01",
            }
        }


class GpuIn(BaseModel):
    pass


class GpuOut(BaseModel):
    pass
