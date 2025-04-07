from typing import List, Optional
from datetime import datetime
from app.schemas.user import UserCreate, UserUpdate
from passlib.context import CryptContext

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# This is a mock service using in-memory storage
# In a real application, you would use a database
class UserService:
    def __init__(self):
        # Mock database
        self.users = [
            {
                "id": 1,
                "email": "admin@example.com",
                "full_name": "Admin User",
                "hashed_password": pwd_context.hash("password123"),
                "is_active": True,
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            },
            {
                "id": 2,
                "email": "user@example.com",
                "full_name": "Regular User",
                "hashed_password": pwd_context.hash("password123"),
                "is_active": True,
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            }
        ]
        self.counter = len(self.users)

    def get_users(self, skip: int = 0, limit: int = 100) -> List[dict]:
        """Get all users with pagination"""
        # Return users without exposing hashed_password
        return [self._remove_password(user) for user in self.users[skip:skip + limit]]

    def get_user(self, user_id: int) -> Optional[dict]:
        """Get a specific user by ID"""
        for user in self.users:
            if user["id"] == user_id:
                return self._remove_password(user)
        return None

    def create_user(self, user: UserCreate) -> dict:
        """Create a new user"""
        # Check if email already exists
        for existing_user in self.users:
            if existing_user["email"] == user.email:
                raise ValueError("Email already registered")
        
        self.counter += 1
        now = datetime.now()
        new_user = {
            "id": self.counter,
            "email": user.email,
            "full_name": user.full_name,
            "hashed_password": pwd_context.hash(user.password),
            "is_active": user.is_active,
            "created_at": now,
            "updated_at": now
        }
        self.users.append(new_user)
        return self._remove_password(new_user)

    def update_user(self, user_id: int, user_update: UserUpdate) -> Optional[dict]:
        """Update an existing user"""
        for i, user in enumerate(self.users):
            if user["id"] == user_id:
                # Update only provided fields
                update_data = user_update.dict(exclude_unset=True)
                
                # Handle password separately
                if "password" in update_data:
                    self.users[i]["hashed_password"] = pwd_context.hash(update_data.pop("password"))
                
                # Update other fields
                for key, value in update_data.items():
                    if value is not None:
                        self.users[i][key] = value
                
                self.users[i]["updated_at"] = datetime.now()
                return self._remove_password(self.users[i])
        return None

    def delete_user(self, user_id: int) -> bool:
        """Delete a user"""
        for i, user in enumerate(self.users):
            if user["id"] == user_id:
                self.users.pop(i)
                return True
        return False
    
    def _remove_password(self, user: dict) -> dict:
        """Remove hashed_password from user dict for security"""
        user_copy = user.copy()
        user_copy.pop("hashed_password", None)
        return user_copy
