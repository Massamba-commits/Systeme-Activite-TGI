from models.user import User
from database.db import Database
<<<<<<< HEAD
=======
from authentification.auth import Auth
>>>>>>> a17c433 (Initialisation du projet complet (Front + Back + DB))

class UserController:
    def __init__(self):
        self.db = Database()
        self.user = User(self.db)
<<<<<<< HEAD
=======
        # Authentication helper lie au modele utilisateur
        self.auth = Auth(self.user)
>>>>>>> a17c433 (Initialisation du projet complet (Front + Back + DB))

    def register(self, data):
        return self.user.create(
            data["username"],
            data["email"],
            data["password"]
        )

<<<<<<< HEAD
    def login(self, auth, data):
        return auth.login(data["username"], data["password"])
=======
    def login(self, data):
        """Retourne un tuple (success, user)"""
        return self.auth.login(data["username"], data["password"])
>>>>>>> a17c433 (Initialisation du projet complet (Front + Back + DB))
