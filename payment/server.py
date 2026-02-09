from flask import Flask, request, jsonify
from flask_cors import CORS
import os, sys

# Ensure local package import works
ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, ROOT)

from payment import Payment

app = Flask(__name__)
CORS(app)
payment_service = Payment()

@app.route('/create_payment', methods=['POST'])
def create_payment():
    data = request.get_json() or {}
    user_id = data.get('user_id')
    item_name = data.get('item_name')
    amount = data.get('amount')
    try:
        amount = int(amount)
    except Exception:
        pass
    method = data.get('method')
    success_url = data.get('success_url', 'http://localhost:8000/success.html')
    cancel_url = data.get('cancel_url', 'http://localhost:8000/cancel.html')
    ipn_url = data.get('ipn_url', '')

    res = payment_service.create_payment(user_id, item_name, amount, method, success_url, cancel_url, ipn_url)
    return jsonify(res)

@app.route('/')
def root():
    return 'Serveur de paiement (simulation)'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
