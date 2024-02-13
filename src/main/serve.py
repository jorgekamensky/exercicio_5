from flask import Flask
from flask_cors import CORS
from .routes import post_user_routes_bp

app = Flask(__name__)
CORS(app)


app.register_blueprint(post_user_routes_bp)
