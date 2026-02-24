import mysql.connector

class Database:
    """Wrapper simple pour la connexion MySQL.

    Utilisé par les modèles pour obtenir un objet connect().
    """

    def __init__(self):
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "tgi_authetification",  # orthographe exacte
        }

    def connect(self):
        return mysql.connector.connect(**self.config)


# Pour debug rapide, on peut exécuter une petite requête si le module est lancé directement
if __name__ == "__main__":
    db = Database()
    conn = db.connect()
    print("Connexion réussie :", conn)
    conn.close()
