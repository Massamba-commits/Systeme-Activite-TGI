from models.transaction import Transaction
from database.db import Database

class TransactionController:
    def __init__(self):
        self.db = Database()
        self.transaction = Transaction(self.db)

    def add(self, user_id, data):
        self.transaction.add(
            user_id,
            data["type"],
            data["montant"]
        )

    def list(self, user_id):
        return self.transaction.list_by_user(user_id)
