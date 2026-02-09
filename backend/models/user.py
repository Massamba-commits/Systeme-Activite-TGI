import hashlib

class User:
    def __init__(self, db):
        self.db = db

    def create(self, username, email, password):
        hashed = hashlib.hashpw(password.encode(), hashlib.gensalt()).decode()

        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, email, password)
            VALUES (%s, %s, %s)
        """, (username, email, hashed))
        conn.commit()

        user_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return user_id

    def get_by_username(self, username):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT id, username, email, password
            FROM users WHERE username=%s
        """, (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user
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
