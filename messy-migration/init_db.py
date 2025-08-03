# init_db.py
import os
from project import create_app, db
from project.models import User

# Delete the old database file if it exists
if os.path.exists('project/users.db'):
    os.remove('project/users.db')

app = create_app()

with app.app_context():
    db.create_all()

    # Create users with hashed passwords
    user1 = User(name='John Doe', email='john@example.com')
    user1.set_password('password123')

    user2 = User(name='Jane Smith', email='jane@example.com')
    user2.set_password('secret456')
    
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

print("Database initialized and seeded.")