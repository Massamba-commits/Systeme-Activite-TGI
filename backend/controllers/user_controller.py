from models.user import User
from database.db import Database

class UserController:
    def __init__(self):
        self.db = Database()
        self.user = User(self.db)

    def register(self, data):
        return self.user.create(
            data["username"],
            data["email"],
            data["password"]
        )

    def login(self, auth, data):
        return auth.login(data["username"], data["password"])
