from typing import Dict
from flask import Blueprint, request, jsonify
user_routes_bp = Blueprint("api_routes", __name__)

from src.main.adapter.request_adapter import request_adapter
from src.main.composer.post_user_composer import post_user_composer
from src.main.composer.get_user_composer import get_user_composer


@user_routes_bp.route("/post", methods=["POST"])
def post_user():
    post_user_view = post_user_composer()
    http_request = request_adapter(request)
    http_response = post_user_view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@user_routes_bp.route("/get", methods=["GET"])
def get_user():
    get_user_view = get_user_composer()
    
    http_request = request_adapter(request)
    http_response = get_user_view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
