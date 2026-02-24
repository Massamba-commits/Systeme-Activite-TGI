from flask import Flask, request, jsonify
from flask_cors import CORS
import os, sys

# Assurer que les imports locaux fonctionnent
ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, ROOT)

from payment import Payment

app = Flask(__name__)
CORS(app)

# Service de paiement
payment_service = Payment()

# Route pour créer un paiement
@app.route('/create_payment', methods=['POST'])
def create_payment():
    data = request.get_json() or {}
    user_id = data.get('user_id')
    item_name = data.get('item_name')
    amount = data.get('amount')

    try:
        amount = int(amount)
    except Exception:
        return jsonify({"error": "Montant invalide"})

    method = data.get('method')
    success_url = data.get('success_url', 'http://localhost:8000/success.html')
    cancel_url = data.get('cancel_url', 'http://localhost:8000/cancel.html')
    ipn_url = data.get('ipn_url', 'http://localhost:5000/ipn')  # ✅ URL IPN par défaut

    res = payment_service.create_payment(
        user_id, item_name, amount, method,
        success_url, cancel_url, ipn_url
    )
    return jsonify(res)

# Route IPN (notification Wave/Orange/PayTech)
@app.route('/ipn', methods=['POST'])
def ipn():
    data = request.get_json() or {}
    txn_id = data.get('transaction_id')
    status = data.get('status')
    amount = data.get('amount')

    # Vérifier la signature envoyée par le fournisseur (sécurité à implémenter)
    print(f"IPN reçu: txn_id={txn_id}, status={status}, amount={amount}")

    # Ici tu peux mettre à jour ta base de données ou ton système interne
    return jsonify({"received": True})

# Route racine
@app.route('/')
def root():
    return 'Serveur de paiement (simulation)'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
