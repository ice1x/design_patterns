from repositories.user_repository import UserRepository
from models import User


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, name: str, email: str):
        new_user = User(name=name, email=email)
        return self.user_repository.create_user(new_user)

    def get_user(self, user_id: int):
        return self.user_repository.get_user_by_id(user_id)

    def list_users(self):
        return self.user_repository.get_all_users()
