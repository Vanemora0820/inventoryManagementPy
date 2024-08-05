from src.models.user import User
from config import db

class UserService:
    def get_all_users(self):
        users = User.query.all()
        return [self.to_dict(user) for user in users]

    def add_user(self, data):
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user.to_dict(user)

  
