from typing import Dict
from .interface.post_user_interface import PostUserInterface
from src.models.user_model import User
from src.models.repo import UserRepo

class PostUserController(PostUserInterface):

    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    def insert_user(self, input_user: Dict):
        try:
            user = User(**input_user)
            self.user_repo.post_user(user)
            return user
        except Exception as e:
            print(f"Error: {e}")
