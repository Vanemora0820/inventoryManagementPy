from flask import Blueprint, request, jsonify
from src.services.user_service import UserService

user_bp = Blueprint('user_bp', __name__)

service = UserService ()

@user_bp.route('', methods=['GET'])
def get_users():
    users = service.get_all_users()
    return jsonify (users), 200


@user_bp.route('', methods=['POST'])
def add_user():
    data = request.json
    user = service.add_user(data)
    return jsonify(user), 201



