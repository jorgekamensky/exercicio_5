from flask import Flask
from flask_cors import CORS
from .routes import user_routes_bp

app = Flask(__name__)
CORS(app)


app.register_blueprint(user_routes_bp)
