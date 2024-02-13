from typing import Dict
from .interface.user_interface import UserInterface
from src.models.user_model import User
from src.models.repo import UserRepo

class PostUserController(UserInterface):

    # def __init__(self, user_repo: UserRepo):
    #     self.user_repo = user_repo

    def save_user(self, input_user: Dict):
        try:
            user = User(**input_user) # unpacking o dict
            user_repo = UserRepo()
            user_repo.post_user(user)
        except Exception as e:
            print(f"Error creating user: {e}")
