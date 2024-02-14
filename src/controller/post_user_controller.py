from typing import Dict
from .interface.post_user_interface import PostUserInterface
from src.models.user_model import User
from src.models.repo import UserRepo

class PostUserController(PostUserInterface):

    # def __init__(self, user_repo: UserRepo):
    #     self.user_repo = user_repo

    def save_user(self, input_user: Dict):
        try:
            user = User(**input_user) # unpacking o dict
            user_repo = UserRepo()
            user_repo.post_user(user)
            return {"msg": "User registered", "content": input_user}
        except Exception as e:
            return (print(f"Error creating user: {e}"))
