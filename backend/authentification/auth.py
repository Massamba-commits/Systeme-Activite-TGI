import bcrypt

class Auth:
    def __init__(self, user_model):
        self.user = user_model

    def hash_password(self, password: str) -> str:
        """Retourne un hash bcrypt encodé en str."""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode()

    def verify_password(self, password: str, hashed: str) -> bool:
        """Vérifie que le mot de passe correspond au hash stocké."""
        return bcrypt.checkpw(password.encode(), hashed.encode())

    def login(self, username: str, password: str):
        """Tente une connexion et renvoie (success, user)."""
        user = self.user.get_by_username(username)
        if not user:
            return False, None

        if self.verify_password(password, user["password"]):
            return True, user
        return False, None
