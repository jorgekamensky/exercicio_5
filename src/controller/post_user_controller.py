from typing import Dict
from .interface.user_interface import UserInterface
from src.database.db_config import connect_db
from src.models.user_model import User

class PostUserController(UserInterface):
    def post_user(self, input_user: Dict):
        user = User(**input_user) # unpacking o dict
        return user
