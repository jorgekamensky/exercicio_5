from .user_model import User
from src.database.db_config import connect_db
from .interface.repo_interface import RepoInterface

class UserRepo(RepoInterface):
    def __init__(self):
        self.db_connection = connect_db()
    
    def post_user(self, user: User):

        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO users (first_name, second_name, full_name) VALUES (?, ?, ?)",
                       (user.first_name, user.second_name, user.full_name))
        self.db_connection.commit()
        
    def delete_user(self):
        pass
    
    def get_user(self, query_param: str): # aqui eu preciso de um model?

        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM users WHERE first_name LIKE ?", ('%' + query_param + '%',))
        user_data = cursor.fetchall()

        if user_data:
            users_list = []
            for row in user_data:
                user_dict = {
                    "first_name": row[0],
                    "second_name": row[1],
                    "full_name": row[2],
                }
                users_list.append(user_dict)
            return users_list
        else:
            return None