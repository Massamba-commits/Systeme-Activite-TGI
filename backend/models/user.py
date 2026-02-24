import bcrypt

class User:
    def __init__(self, db):
        self.db = db

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
        conn.commit()

        user_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return user_id

    def get_by_username(self, username: str):
        """Récupère un utilisateur par son username."""
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT id, username, email, password
            FROM users WHERE username=%s
            """,
            (username,)
        )
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user