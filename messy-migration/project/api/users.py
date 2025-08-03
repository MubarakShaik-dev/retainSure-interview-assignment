# project/api/users.py
from flask import Blueprint, request, jsonify
from project import services
from flask_jwt_extended import create_access_token

users_bp = Blueprint('users_api', __name__)

@users_bp.route('/')
def health_check():
    return jsonify({"status": "ok", "message": "User Management System is running"})

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = services.get_all_users()
    return jsonify([user.to_dict() for user in users]), 200

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user, error = services.create_user(data)
    if error:
        return jsonify({"error": error}), 400
    return jsonify(new_user.to_dict()), 201

@users_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = services.get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200

@users_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user, error = services.update_user(user_id, data)
    if error:
        return jsonify({"error": error}), 404
    return jsonify(user.to_dict()), 200

@users_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success, error = services.delete_user(user_id)
    if error:
        return jsonify({"error": error}), 404
    return '', 204

@users_bp.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Query parameter 'name' is required"}), 400
    users = services.search_users_by_name(name)
    return jsonify([user.to_dict() for user in users]), 200

@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400
        
    user = services.authenticate_user(email, password)
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401
        
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200