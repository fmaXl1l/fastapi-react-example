from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from app.schemas.user import User, UserCreate, UserUpdate
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "User not found"}},
)

# Dependency to get the user service
def get_user_service():
    return UserService()

@router.get("/", response_model=List[User])
async def read_users(
    skip: int = 0, 
    limit: int = 100, 
    user_service: UserService = Depends(get_user_service)
):
    """
    Retrieve users with pagination.
    """
    return user_service.get_users(skip=skip, limit=limit)

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate, 
    user_service: UserService = Depends(get_user_service)
):
    """
    Create a new user.
    """
    return user_service.create_user(user)

@router.get("/{user_id}", response_model=User)
async def read_user(
    user_id: int, 
    user_service: UserService = Depends(get_user_service)
):
    """
    Get a specific user by ID.
    """
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
async def update_user(
    user_id: int, 
    user: UserUpdate, 
    user_service: UserService = Depends(get_user_service)
):
    """
    Update a user.
    """
    updated_user = user_service.update_user(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int, 
    user_service: UserService = Depends(get_user_service)
):
    """
    Delete a user.
    """
    success = user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return None
