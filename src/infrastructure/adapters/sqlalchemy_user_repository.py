from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import or_
from src.core.interfaces.user_manager import IUserManager
from src.core.entities.user import User
from src.core.entities.plan import Plan
from werkzeug.security import generate_password_hash, check_password_hash

class SQLAlchemyUserRepository(IUserManager):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def register_user(self, username: str, email: str, password: str) -> User:
        async with self.session.begin():
            # Check if username or email already exists
            existing_user = await self.session.execute(
                select(User).where(or_(User.username == username, User.email == email))
            )
            if existing_user.scalar_one_or_none():
                raise ValueError("Username or email already taken")

            new_user = User(username=username, email=email)
            new_user.set_password(password)
            self.session.add(new_user)
            await self.session.flush()
            return new_user

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        async with self.session.begin():
            result = await self.session.execute(select(User).filter(User.id == user_id))
            return result.scalar_one_or_none()

    async def get_user_by_username(self, username: str) -> Optional[User]:
        async with self.session.begin():
            result = await self.session.execute(select(User).filter(User.username == username))
            return result.scalar_one_or_none()

    async def get_user_by_email(self, email: str) -> Optional[User]:
        async with self.session.begin():
            result = await self.session.execute(select(User).filter(User.email == email))
            return result.scalar_one_or_none()

    async def update_user(self, user: User) -> User:
        async with self.session.begin():
            await self.session.merge(user)
            return user

    async def delete_user(self, user_id: int) -> bool:
        async with self.session.begin():
            user = await self.get_user_by_id(user_id)
            if user:
                await self.session.delete(user)
                return True
            return False

    async def authenticate_user(self, username: str, password: str) -> Optional[User]:
        user = await self.get_user_by_username(username)
        if user and user.check_password(password):
            return user
        return None

    async def change_password(self, user_id: int, old_password: str, new_password: str) -> bool:
        async with self.session.begin():
            user = await self.get_user_by_id(user_id)
            if user and user.check_password(old_password):
                user.set_password(new_password)
                await self.session.merge(user)
                return True
            return False

    async def get_user_plan(self, user_id: int) -> Plan:
        user = await self.get_user_by_id(user_id)
        if user:
            # Assuming Plan is an Enum or a simple object. You might need to adjust this
            # based on your actual Plan implementation
            return Plan.PREMIUM if user.is_subscribed else Plan.FREE
        raise ValueError("User not found")

    async def update_user_plan(self, user_id: int, plan_id: int) -> User:
        async with self.session.begin():
            user = await self.get_user_by_id(user_id)
            if user:
                # Assuming plan_id 1 is free and 2 is premium. Adjust as needed.
                user.is_subscribed = (plan_id == 2)
                await self.session.merge(user)
                return user
            raise ValueError("User not found")

    async def get_all_users(self, page: int = 1, per_page: int = 20) -> List[User]:
        async with self.session.begin():
            result = await self.session.execute(
                select(User)
                .order_by(User.id)
                .offset((page - 1) * per_page)
                .limit(per_page)
            )
            return result.scalars().all()

    async def search_users(self, query: str, page: int = 1, per_page: int = 20) -> List[User]:
        async with self.session.begin():
            result = await self.session.execute(
                select(User)
                .where(or_(User.username.ilike(f"%{query}%"), User.email.ilike(f"%{query}%")))
                .order_by(User.id)
                .offset((page - 1) * per_page)
                .limit(per_page)
            )
            return result.scalars().all()