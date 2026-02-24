<<<<<<< HEAD
# On importe la bibliothèque qui permet à Python de communiquer avec MySQL
import mysql.connector


# On crée une connexion avec la base de données MySQL
bd = mysql.connector.connect(
    host="localhost",     # Adresse du serveur MySQL (localhost = ton PC)
    user="root",          # Nom d'utilisateur MySQL (root par défaut dans XAMPP)
    password="",          # Mot de passe MySQL (vide par défaut dans XAMPP)
    database="tgi_authetification"      # Nom de la base de données à utiliser
)


# Affiche un message si la connexion s’est bien faite
print("Connexion réussie")


# Création d’un curseur
# Le curseur sert à envoyer des commandes SQL à la base de données
cursor = bd.cursor()


# On envoie une requête SQL à la base
# Ici on demande : "sélectionne toutes les données de la table chambre"
cursor.execute("desc users")


# fetchall() récupère toutes les lignes retournées par la requête SQL
# La boucle parcourt chaque ligne récupérée
for users in cursor.fetchall():
    
    # Affiche chaque ligne de la table chambre
    print(users)
=======
import mysql.connector

class Database:
    """Wrapper simple pour la connexion MySQL.

    Utilise par les modeles pour obtenir un objet connect().
    """

    def __init__(self):
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            # Conserver le nom de base tel qu'actuel (orthographe exacte)
            "database": "tgi_authetification",
        }

    def connect(self):
        return mysql.connector.connect(**self.config)


# Pour debug rapide, on peut executer une petite requete si le module est lance
if __name__ == "__main__":
    db = Database()
    conn = db.connect()
    print("connexion r�ussie", conn)
    conn.close()
>>>>>>> a17c433 (Initialisation du projet complet (Front + Back + DB))
