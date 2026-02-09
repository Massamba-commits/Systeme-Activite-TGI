from flask import Flask
from routes.user_routers import user_routes
from routes.transaction_routers import transaction_routes

app = Flask(__name__)
app.secret_key = "secret123"

app.register_blueprint(user_routes, url_prefix="/api")
app.register_blueprint(transaction_routes, url_prefix="/api")

app.run(debug=True)
