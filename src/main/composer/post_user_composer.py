from typing import Dict
from src.views.post_user_view import PostUserView
from src.controller.post_user_controller import PostUserController
from src.models.repo import UserRepo

def post_user_composer():
    user_repo = UserRepo()
    post_user_controller = PostUserController(user_repo)
    post_user_view = PostUserView(post_user_controller)
    return post_user_view