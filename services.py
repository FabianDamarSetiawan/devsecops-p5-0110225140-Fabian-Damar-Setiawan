from models import User

class UserService:
    def __init__(self):
        self.users = [
            User(1, "admin", "admin@sec.local"),
            User(2, "developer", "dev@sec.local")
        ]

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def add_user(self, user_id, username, email):
        new_user = User(user_id, username, email)
        self.users.append(new_user)
        return new_user