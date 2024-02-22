from typing import Dict
from src.views.post_user_view import PostUserView
from src.controller.post_user_controller import PostUserController

def post_user_composer(input_user: Dict):
    post_user_controller = PostUserController(input_user)
    post_user_view = PostUserView(post_user_controller)
    return post_user_view