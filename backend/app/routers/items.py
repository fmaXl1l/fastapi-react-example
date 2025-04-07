from fastapi import APIRouter, HTTPException, Depends, status
from typing import List, Optional
from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.services.item_service import ItemService

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Item not found"}},
)

# Dependency to get the item service
def get_item_service():
    return ItemService()

@router.get("/", response_model=List[Item])
async def read_items(
    skip: int = 0, 
    limit: int = 100, 
    item_service: ItemService = Depends(get_item_service)
):
    """
    Retrieve items with pagination.
    """
    return item_service.get_items(skip=skip, limit=limit)

@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(
    item: ItemCreate, 
    item_service: ItemService = Depends(get_item_service)
):
    """
    Create a new item.
    """
    return item_service.create_item(item)

@router.get("/{item_id}", response_model=Item)
async def read_item(
    item_id: int, 
    item_service: ItemService = Depends(get_item_service)
):
    """
    Get a specific item by ID.
    """
    item = item_service.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=Item)
async def update_item(
    item_id: int, 
    item: ItemUpdate, 
    item_service: ItemService = Depends(get_item_service)
):
    """
    Update an item.
    """
    updated_item = item_service.update_item(item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(
    item_id: int, 
    item_service: ItemService = Depends(get_item_service)
):
    """
    Delete an item.
    """
    success = item_service.delete_item(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return None
