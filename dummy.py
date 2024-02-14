from src.controller.get_user_controller import GetUserController

def main():

    # user_repo = UserRepo()
    # user_controller = PostUserController(user_repo)
    # input_user = {"first_name": 'jorge 2', "second_name": 'kamensky 2'}
    # user_controller.save_user(input_user)
    # print("Usuário criado e salvo com sucesso!")

    user_query = "luis"
    user_controller = GetUserController()
    v = user_controller.query_user(user_query)
    print(v)

if __name__ == "__main__":
    main()