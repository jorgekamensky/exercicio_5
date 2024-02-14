from src.views.get_user_view import GetUserView
from src.controller.get_user_controller import GetUserController

def get_user_composer():
    get_user_controller = GetUserController()
    get_user_view = GetUserView(get_user_controller)
    return get_user_view
