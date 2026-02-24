<<<<<<< HEAD
import hashlib
=======
import bcrypt
>>>>>>> a17c433 (Initialisation du projet complet (Front + Back + DB))

class User:
    def __init__(self, db):
        self.db = db

<<<<<<< HEAD
    def create(self, username, email, password):
        hashed = hashlib.hashpw(password.encode(), hashlib.gensalt()).decode()

        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, email, password)
            VALUES (%s, %s, %s)
        """, (username, email, hashed))
=======
    def create(self, username: str, email: str, password: str):
        """Enregistre un nouvel utilisateur et retourne son id."""
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO users (username, email, password)
            VALUES (%s, %s, %s)
            """,
            (username, email, hashed)
        )
>>>>>>> a17c433 (Initialisation du projet complet (Front + Back + DB))
        conn.commit()

        user_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return user_id

<<<<<<< HEAD
    def get_by_username(self, username):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT id, username, email, password
            FROM users WHERE username=%s
        """, (username,))
=======
    def get_by_username(self, username: str):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT id, username, email, password
            FROM users WHERE username=%s
            """,
            (username,)
        )
>>>>>>> a17c433 (Initialisation du projet complet (Front + Back + DB))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user
<<<<<<< HEAD
    def _init_(self, db):
        self.db = db

    def register(self, username, email, password_hash):
        """Inscription d'un nouvel utilisateur"""
        cursor = self.db.conn.cursor()
        cursor.execute(
            "INSERT INTO inscription (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, password_hash)
        )
        self.db.conn.commit()
        return cursor.lastrowid

    def get_user(self, username):
        """Récupère un utilisateur par son username"""
        cursor = self.db.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM inscription WHERE username=%s", (username,))
        return cursor.fetchone()
=======
>>>>>>> a17c433 (Initialisation du projet complet (Front + Back + DB))
