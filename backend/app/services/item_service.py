from typing import List, Optional
from datetime import datetime
from app.schemas.item import ItemCreate, ItemUpdate

# This is a mock service using in-memory storage
# In a real application, you would use a database
class ItemService:
    def __init__(self):
        # Mock database
        self.items = [
            {
                "id": 1,
                "title": "Laptop",
                "description": "High-performance laptop for developers",
                "price": 1299.99,
                "available": True,
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            },
            {
                "id": 2,
                "title": "Smartphone",
                "description": "Latest smartphone with advanced camera",
                "price": 899.99,
                "available": True,
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            }
        ]
        self.counter = len(self.items)

    def get_items(self, skip: int = 0, limit: int = 100) -> List[dict]:
        """Get all items with pagination"""
        return self.items[skip:skip + limit]

    def get_item(self, item_id: int) -> Optional[dict]:
        """Get a specific item by ID"""
        for item in self.items:
            if item["id"] == item_id:
                return item
        return None

    def create_item(self, item: ItemCreate) -> dict:
        """Create a new item"""
        self.counter += 1
        now = datetime.now()
        new_item = {
            "id": self.counter,
            "title": item.title,
            "description": item.description,
            "price": item.price,
            "available": item.available,
            "created_at": now,
            "updated_at": now
        }
        self.items.append(new_item)
        return new_item

    def update_item(self, item_id: int, item_update: ItemUpdate) -> Optional[dict]:
        """Update an existing item"""
        for i, item in enumerate(self.items):
            if item["id"] == item_id:
                # Update only provided fields
                update_data = item_update.dict(exclude_unset=True)
                for key, value in update_data.items():
                    if value is not None:
                        self.items[i][key] = value
                self.items[i]["updated_at"] = datetime.now()
                return self.items[i]
        return None

    def delete_item(self, item_id: int) -> bool:
        """Delete an item"""
        for i, item in enumerate(self.items):
            if item["id"] == item_id:
                self.items.pop(i)
                return True
        return False
