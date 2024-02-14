from typing import Dict
from .interface.get_user_interface import GetUserInterface
from src.models.repo import UserRepo

class GetUserController(GetUserInterface):

    def query_user(self, query_param: str) -> Dict:
        try:
            
            user_repo = UserRepo()
            users_data = user_repo.get_user(query_param)

            if users_data:
                return users_data
            else:
                return []
        except Exception as e:
            print(f"Error with query: {e}")
