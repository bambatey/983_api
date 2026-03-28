from sqlalchemy.ext.asyncio import AsyncSession
from datalayer.repository._base_repository import AsyncBaseRepository
from datalayer.model.db.auth import Auth
from typing import List, Optional

class AuthService:
    def __init__(self, session: AsyncSession):
        self.repository = AsyncBaseRepository(session, Auth)

    async def register_user(self, user_data: dict) -> Auth:
        # Simple registration logic
        user = Auth(
            user_name=user_data["username"],
            user_email=user_data["email"],
            user_password=user_data["password"]  # In real app, hash this!
        )
        return await self.repository.save(user)

    async def get_user_by_username(self, username: str) -> Optional[Auth]:
        # Using user_name field
        return await self.repository.find_one_by(user_name=username)

    async def get_all_users(self) -> List[Auth]:
        return await self.repository.get_all()
