from flask import Flask
from routes.user_routers import user_routes
from routes.transaction_routers import transaction_routes
from flask import Flask, request, jsonify

app = Flask(__name__)
app.secret_key = "secret123"

app.register_blueprint(user_routes, url_prefix="/api")
app.register_blueprint(transaction_routes, url_prefix="/api")

app.run(debug=True)

# -------------------------------
# Routes Utilisateurs (API)
# -------------------------------
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    # Exemple simple d'authentification
    if username == "admin" and password == "1234":
        return jsonify({"message": "Connexion réussie"}), 200
    return jsonify({"error": "Identifiants invalides"}), 401


# -------------------------------
# Routes Transactions (API)
# -------------------------------
@app.route("/api/transactions", methods=["GET"])
def list_transactions():
    # Exemple fictif
    transactions = [
        {"id": 1, "user_id": 2, "amount": 5000, "status": "SUCCESS"},
        {"id": 2, "user_id": 3, "amount": 3000, "status": "PENDING"}
    ]
    return jsonify(transactions), 200


# -------------------------------
# Point d’entrée
# -------------------------------
if __name__ == "__main__":
    # host="0.0.0.0" permet d'accéder depuis le réseau local
    app.run(debug=True, host="0.0.0.0", port=5000)
