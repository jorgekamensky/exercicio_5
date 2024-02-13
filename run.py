from src.database.db_config import start_db
from src.main.serve import app

if __name__ == "__main__":
    start_db()
    app.run(host="0.0.0.0", port=3000)