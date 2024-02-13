from flask import Blueprint, request, jsonify
post_user_routes_bp = Blueprint("api_routes", __name__)

from src.main.adapter.request_adapter import request_adapter
from src.main.composer.post_user_composer import post_user_composer


@post_user_routes_bp.route("/post", methods=["POST"])
def post_user():
    post_user_view = post_user_composer()
    
    http_request = request_adapter(request)
    http_response = post_user_view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
