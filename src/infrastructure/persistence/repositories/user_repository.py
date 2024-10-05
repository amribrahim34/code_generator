from typing import List, Optional
from sqlalchemy.orm import Session
from src.core.entities.user import User
from src.core.interfaces.user_manager import IUserManager
from src.infrastructure.persistence.models.user_model import UserModel

class UserRepository(IUserManager):
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user: User) -> User:
        user_model = UserModel(
            id=user.id,
            username=user.username,
            email=user.email,
            password_hash=user.password_hash,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
        self.session.add(user_model)
        self.session.commit()
        return user

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        user_model = self.session.query(UserModel).filter(UserModel.id == user_id).first()
        if user_model:
            return User.from_dict(user_model.__dict__)
        return None

    def get_user_by_email(self, email: str) -> Optional[User]:
        user_model = self.session.query(UserModel).filter(UserModel.email == email).first()
        if user_model:
            return User.from_dict(user_model.__dict__)
        return None

    def get_all_users(self) -> List[User]:
        user_models = self.session.query(UserModel).all()
        return [User.from_dict(user_model.__dict__) for user_model in user_models]

    def update_user(self, user: User) -> User:
        user_model = self.session.query(UserModel).filter(UserModel.id == user.id).first()
        if user_model:
            user_model.username = user.username
            user_model.email = user.email
            user_model.password_hash = user.password_hash
            user_model.is_active = user.is_active
            user_model.updated_at = user.updated_at
            self.session.commit()
        return user

    def delete_user(self, user_id: str) -> bool:
        user_model = self.session.query(UserModel).filter(UserModel.id == user_id).first()
        if user_model:
            self.session.delete(user_model)
            self.session.commit()
            return True
        return False