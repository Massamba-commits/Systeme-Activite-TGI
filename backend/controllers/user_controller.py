from models.user import User
from database.db import Database
from authentification.auth import Auth

class UserController:
    def __init__(self):
        self.db = Database()
        self.user = User(self.db)
        # Authentication helper lié au modèle utilisateur
        self.auth = Auth(self.user)

    def register(self, data):
        return self.user.create(
            data["username"],
            data["email"],
            data["password"]
        )

    def login(self, data):
        """Retourne un tuple (success, user)"""
        return self.auth.login(data["username"], data["password"])
