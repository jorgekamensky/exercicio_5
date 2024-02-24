from typing import Dict
from .interface.get_user_interface import GetUserInterface
## from src.models.repo import UserRepo
from src.models.interface.repo_interface import RepoInterface as UserRepo

class GetUserController(GetUserInterface):

    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    def query_user(self, query_param: str) -> Dict:
        try:            
            ##user_repo = UserRepo()
            users_data = self.user_repo.get_user(query_param)
            if users_data:
                return users_data
            else:
                return []
        except Exception as e:
            print(f"Error with query: {e}")
