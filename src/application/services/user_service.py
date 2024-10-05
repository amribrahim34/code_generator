from typing import List, Optional
from datetime import datetime
from passlib.hash import bcrypt
from src.core.interfaces.user_manager import IUserManager
from src.core.entities.user import User
from src.core.entities.plan import Plan
from src.infrastructure.persistence.repositories.user_repository import UserRepository
from src.infrastructure.persistence.repositories.plan_repository import PlanRepository
from src.application.dtos.user_dtos import UserDTO, UserCreateDTO, UserUpdateDTO, UserProfileDTO, UserListDTO

class UserService(IUserManager):
    def __init__(self, user_repository: UserRepository, plan_repository: PlanRepository):
        self.user_repository = user_repository
        self.plan_repository = plan_repository

    async def register_user(self, username: str, email: str, password: str) -> User:
        if await self.get_user_by_username(username):
            raise ValueError("Username is already taken")
        if await self.get_user_by_email(email):
            raise ValueError("Email is already registered")
        
        hashed_password = bcrypt.hash(password)
        user = User(username=username, email=email, password_hash=hashed_password)
        return await self.user_repository.create(user)

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        return await self.user_repository.get_by_id(user_id)

    async def get_user_by_username(self, username: str) -> Optional[User]:
        return await self.user_repository.get_by_username(username)

    async def get_user_by_email(self, email: str) -> Optional[User]:
        return await self.user_repository.get_by_email(email)

    async def update_user(self, user: User) -> User:
        existing_user = await self.get_user_by_id(user.id)
        if not existing_user:
            raise ValueError(f"User with id {user.id} does not exist")
        return await self.user_repository.update(user)

    async def delete_user(self, user_id: int) -> bool:
        return await self.user_repository.delete(user_id)

    async def authenticate_user(self, username: str, password: str) -> Optional[User]:
        user = await self.get_user_by_username(username)
        if user and bcrypt.verify(password, user.password_hash):
            user.last_login = datetime.utcnow()
            await self.update_user(user)
            return user
        return None

    async def change_password(self, user_id: int, old_password: str, new_password: str) -> bool:
        user = await self.get_user_by_id(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} does not exist")
        
        if not bcrypt.verify(old_password, user.password_hash):
            raise ValueError("Old password is incorrect")
        
        user.password_hash = bcrypt.hash(new_password)
        await self.update_user(user)
        return True

    async def get_user_plan(self, user_id: int) -> Plan:
        user = await self.get_user_by_id(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} does not exist")
        return user.plan

    async def update_user_plan(self, user_id: int, plan_id: int) -> User:
        user = await self.get_user_by_id(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} does not exist")
        
        plan = await self.plan_repository.get_by_id(plan_id)
        if not plan:
            raise ValueError(f"Plan with id {plan_id} does not exist")
        
        user.plan = plan
        return await self.update_user(user)

    async def get_all_users(self, page: int = 1, per_page: int = 20) -> List[User]:
        return await self.user_repository.get_all(page, per_page)

    async def search_users(self, query: str, page: int = 1, per_page: int = 20) -> List[User]:
        return await self.user_repository.search(query, page, per_page)

    # Helper methods to convert between entities and DTOs
    def _user_to_dto(self, user: User) -> UserDTO:
        return UserDTO(
            id=user.id,
            username=user.username,
            email=user.email,
            created_at=user.created_at,
            is_active=user.is_active,
            is_subscribed=bool(user.plan),
            plan_name=user.plan.name if user.plan else None
        )

    def _user_to_profile_dto(self, user: User, project_count: int) -> UserProfileDTO:
        return UserProfileDTO(
            id=user.id,
            username=user.username,
            email=user.email,
            created_at=user.created_at,
            is_subscribed=bool(user.plan),
            plan_name=user.plan.name if user.plan else None,
            project_count=project_count,
            last_login=user.last_login
        )

    # Additional methods to handle DTOs
    async def create_user_from_dto(self, dto: UserCreateDTO) -> UserDTO:
        user = await self.register_user(dto.username, dto.email, dto.password)
        return self._user_to_dto(user)

    async def update_user_from_dto(self, user_id: int, dto: UserUpdateDTO) -> UserDTO:
        user = await self.get_user_by_id(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} does not exist")
        
        if dto.username:
            user.username = dto.username
        if dto.email:
            user.email = dto.email
        if dto.is_active is not None:
            user.is_active = dto.is_active
        
        updated_user = await self.update_user(user)
        return self._user_to_dto(updated_user)

    async def get_user_profile(self, user_id: int) -> UserProfileDTO:
        user = await self.get_user_by_id(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} does not exist")
        
        project_count = await self.user_repository.get_user_project_count(user_id)
        return self._user_to_profile_dto(user, project_count)

    async def get_users_list(self, page: int = 1, per_page: int = 20) -> UserListDTO:
        users = await self.get_all_users(page, per_page)
        total = await self.user_repository.count()
        return UserListDTO(
            users=[self._user_to_dto(user) for user in users],
            total=total,
            page=page,
            per_page=per_page
        )

    async def search_users_list(self, query: str, page: int = 1, per_page: int = 20) -> UserListDTO:
        users = await self.search_users(query, page, per_page)
        total = await self.user_repository.count_search(query)
        return UserListDTO(
            users=[self._user_to_dto(user) for user in users],
            total=total,
            page=page,
            per_page=per_page
        )