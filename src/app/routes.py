from flask import Blueprint, jsonify
from src.database.queries import get_all_users, get_user_by_id

api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users)

@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)