# project/services.py
from .models import User
from . import db

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def create_user(data):
    """Creates a new user and adds them to the database."""
    if 'name' not in data or 'email' not in data or 'password' not in data:
        return None, "Missing required fields: name, email, password"

    if User.query.filter_by(email=data['email']).first():
        return None, "Email address already in use"

    new_user = User(name=data['name'], email=data['email'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return new_user, None

def update_user(user_id, data):
    """Updates a user's information."""
    user = get_user_by_id(user_id)
    if not user:
        return None, "User not found"
        
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    db.session.commit()
    return user, None

def delete_user(user_id):
    """Deletes a user from the database."""
    user = get_user_by_id(user_id)
    if not user:
        return False, "User not found"
        
    db.session.delete(user)
    db.session.commit()
    return True, None

def search_users_by_name(name):
    """Searches for users by name (case-insensitive)."""
    return User.query.filter(User.name.ilike(f'%{name}%')).all()

def authenticate_user(email, password):
    """Authenticates a user by email and password."""
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    return None