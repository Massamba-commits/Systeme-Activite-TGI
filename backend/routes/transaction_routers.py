from flask import Blueprint, request, jsonify, session
from controllers.transaction_controller import TransactionController

transaction_routes = Blueprint("transaction_routes", __name__)
controller = TransactionController()

@transaction_routes.route("/transactions", methods=["POST"])
def add_transaction():
    if "user_id" not in session:
        return jsonify({"error": "Non autorisé"}), 401

    controller.add(session["user_id"], request.json)
    return jsonify({"message": "Transaction ajoutée"})

@transaction_routes.route("/transactions", methods=["GET"])
def list_transactions():
    if "user_id" not in session:
        return jsonify({"error": "Non autorisé"}), 401

    return jsonify(controller.list(session["user_id"]))
