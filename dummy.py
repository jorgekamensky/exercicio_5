from src.controller.post_user_controller import PostUserController
from src.models.repo import UserRepo

def main():

    user_repo = UserRepo()
    user_controller = PostUserController(user_repo)
    input_user = {"first_name": 'jorge 2', "second_name": 'kamensky 2'}
    user_controller.save_user(input_user)
    print("Usuário criado e salvo com sucesso!")

if __name__ == "__main__":
    main()