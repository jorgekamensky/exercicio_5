from .user_model import User
from src.database.db_config import connect_db

class UserRepo:
    def __init__(self):
        self.db_connection = connect_db()
    
    def post_user(self, user: User):

        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO users (first_name, second_name, full_name) VALUES (?, ?, ?)",
                       (user.first_name, user.second_name, user.full_name))
        self.db_connection.commit()
        
    def delete_user(self):
        pass
    def get_user(self):
        pass