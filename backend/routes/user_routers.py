from flask import Blueprint, request, jsonify, session
from controllers.user_controller import UserController
from authentification.auth import auth

user_routes = Blueprint("user_routes", __name__)
controller = UserController()
auth = auth(controller.user)

@user_routes.route("/register", methods=["POST"])
def register():
    user_id = controller.register(request.json)
    return jsonify({"message": "Utilisateur créé", "id": user_id})

@user_routes.route("/login", methods=["POST"])
def login():
    success, user = controller.login(auth, request.json)

    if not success:
        return jsonify({"error": "Identifiants invalides"}), 401

    session["user_id"] = user["id"]
    return jsonify({"message": "Connexion réussie"})
