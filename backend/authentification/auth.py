import hashlib

class Auth:
<<<<<<< HEAD
    def __init__(self, user_model):
        self.user = user_model

    def login(self, username, password):
=======
    """Gestion simple de l'authentification utilisateur.

    L'instance attend un mod�le user_model poss�dant au minimum
    les m�thodes get_by_username (pour la lecture) et
    un champ password contenant le hash bcrypt.
    """

    def __init__(self, user_model):
        self.user = user_model

    def hash_password(self, password: str) -> str:
        """Retourne un hash bcrypt d�cod� en str.
        Utile pour l'enregistrement.
        """
        salt = hashlib.gensalt()
        return hashlib.hashpw(password.encode(), salt).decode()

    def verify_password(self, password: str, hashed: str) -> bool:
        """V�rifie que le mot de passe correspond au hash stock�."""
        return hashlib.checkpw(password.encode(), hashed.encode())

    def login(self, username: str, password: str):
        """Tente une connexion et renvoie un tuple (success, user).

        success est un bool�en et user est le dictionnaire
        de l'utilisateur si valid� sinon None.
        """
>>>>>>> a17c433 (Initialisation du projet complet (Front + Back + DB))
        user = self.user.get_by_username(username)
        if not user:
            return False, None

<<<<<<< HEAD
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
=======
        if self.verify_password(password, user["password"]):
            return True, user
        return False, None
>>>>>>> a17c433 (Initialisation du projet complet (Front + Back + DB))
