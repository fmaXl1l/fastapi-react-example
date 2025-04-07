from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    """Base schema for user data"""
    email: EmailStr = Field(..., description="User email address")
    full_name: str = Field(..., min_length=1, max_length=100, description="Full name of the user")
    is_active: bool = Field(True, description="Whether the user is active")

class UserCreate(UserBase):
    """Schema for creating a new user"""
    password: str = Field(..., min_length=8, description="User password, minimum 8 characters")

class UserUpdate(BaseModel):
    """Schema for updating a user, all fields are optional"""
    email: Optional[EmailStr] = Field(None, description="User email address")
    full_name: Optional[str] = Field(None, min_length=1, max_length=100, description="Full name of the user")
    is_active: Optional[bool] = Field(None, description="Whether the user is active")
    password: Optional[str] = Field(None, min_length=8, description="User password, minimum 8 characters")

class User(UserBase):
    """Schema for a complete user with ID and timestamps"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
