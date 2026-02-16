import hashlib

class Auth:
    def __init__(self, user_model):
        self.user = user_model

    def login(self, username, password):
        user = self.user.get_by_username(username)
        if not user:
            return False, None

        if not hashlib.checkpw(password.encode(), user["password"].encode()):
            return False, None

        return True, user
class Auth:
    def _init_(self, user):
        self.user = user

    def hash_password(self, password):
        """Hashage sécurisé du mot de passe avec bcrypt"""
        salt = hashlib.gensalt()
        return hashlib.hashpw(password.encode(), salt)

    def verify_password(self, password, hashed):
        """Vérifie si le mot de passe correspond au hash"""
        return hashlib.checkpw(password.encode(), hashed.encode())

    def login(self, username, password):
        """Connexion sécurisée"""
        user = self.user.get_user(username)
        if user and self.verify_password(password, user["password_hash"]):
            return True
        return False