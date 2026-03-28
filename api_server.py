from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

app = Flask(__name__)

# JWT Config
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Dummy DB
users = [
    {"id": 1, "username": "admin", "password": "admin123"},
    {"id": 2, "username": "user", "password": "password"}
]

orders = [
    {"order_id":1, "user_id":1, "item":"Laptop"},
    {"order_id":2, "user_id":2, "item":"Phone"}
]

# HOME
@app.route("/")
def home():
    return jsonify({"message": "API is running"})

# LOGIN (JWT)
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    for user in users:
        if user["username"] == data.get("username") and user["password"] == data.get("password"):
            
            token = create_access_token(identity=str(user["id"]))

            return jsonify({
                "message": "Login successful",
                "token": token
            })

    return jsonify({"message": "Invalid credentials"}), 401

# GOOGLE LOGIN WIP
# OAUTH (SIMULATED)
@app.route("/oauth/login", methods=["GET"])
def oauth_login():
    # Simulated OAuth login (for testing)
    fake_user = {"id": 3, "username": "google_user"}
    token = create_access_token(identity=str(fake_user["id"]))

    return jsonify({
        "message": "OAuth login success",
        "token": token
    })


# GET USERS (Protected)
@app.route("/users", methods=["GET"])
@jwt_required()
def get_users():
    return jsonify(users)


# PROFILE (BOLA Vulnerable)
@app.route("/profile/<int:user_id>", methods=["GET"])
@jwt_required()
def profile(user_id):

    current_user = get_jwt_identity()

    # Intentional vulnerability (no authorization check)
    for user in users:
        if user["id"] == user_id:
            return jsonify({
                "requested_by": current_user,
                "data": user
            })

    return jsonify({"message":"User not found"})


# ORDERS (BOLA Vulnerable)
@app.route("/orders/<int:user_id>", methods=["GET"])
@jwt_required()
def get_orders(user_id):

    # No check if user owns the orders
    user_orders = [o for o in orders if o["user_id"] == user_id]

    return jsonify(user_orders)


# Secure Version (No BOLA Vulnerability)
@app.route("/secure/orders", methods=["GET"])
@jwt_required()
def secure_orders():

    current_user = get_jwt_identity()

    user_orders = [o for o in orders if o["user_id"] == current_user]

    return jsonify(user_orders)


# Multiple Requests Limit (Maximum 5)
request_count = {}

@app.route("/limited", methods=["GET"])
def limited():

    ip = request.remote_addr

    request_count[ip] = request_count.get(ip, 0) + 1

    if request_count[ip] > 5:
        return jsonify({"message": "Rate limit exceeded"}), 429

    return jsonify({"message": "Request allowed", "count": request_count[ip]})


# Run in outside environment (For POSTMAN outisde VM) 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
