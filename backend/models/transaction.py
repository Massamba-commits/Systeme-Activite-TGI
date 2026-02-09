class Transaction:
    def __init__(self, db):
        self.db = db

    def add(self, user_id, type_transaction, montant, statut="en_attente"):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO transactions (user_id, type, montant, statut)
            VALUES (%s, %s, %s, %s)
        """, (user_id, type_transaction, montant, statut))
        conn.commit()
        cursor.close()
        conn.close()

    def list_by_user(self, user_id):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT id, type, montant, statut, created_at
            FROM transactions WHERE user_id=%s
        """, (user_id,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
