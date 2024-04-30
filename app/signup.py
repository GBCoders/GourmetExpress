from .app import db
from .models import User

# estou em duvida se aciono o id, ele é criado sozinho
def register_user(username, email, password):
    if not User.query.filter_by(username=username).first():
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return True
    else:
        return False
