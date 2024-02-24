from src.views.get_user_view import GetUserView
from src.controller.get_user_controller import GetUserController
from src.models.repo import UserRepo

def get_user_composer():
    user_repo = UserRepo()
    get_user_controller = GetUserController(user_repo)
    get_user_view = GetUserView(get_user_controller)
    return get_user_view
