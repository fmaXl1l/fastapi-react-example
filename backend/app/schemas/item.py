from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ItemBase(BaseModel):
    """Base schema for item data"""
    title: str = Field(..., min_length=1, max_length=100, description="Title of the item")
    description: Optional[str] = Field(None, max_length=1000, description="Optional description of the item")
    price: float = Field(..., ge=0, description="Price of the item, must be non-negative")
    available: bool = Field(True, description="Whether the item is available")

class ItemCreate(ItemBase):
    """Schema for creating a new item"""
    pass

class ItemUpdate(BaseModel):
    """Schema for updating an item, all fields are optional"""
    title: Optional[str] = Field(None, min_length=1, max_length=100, description="Title of the item")
    description: Optional[str] = Field(None, max_length=1000, description="Optional description of the item")
    price: Optional[float] = Field(None, ge=0, description="Price of the item, must be non-negative")
    available: Optional[bool] = Field(None, description="Whether the item is available")

class Item(ItemBase):
    """Schema for a complete item with ID and timestamps"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
