from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "username": "admin", "password": "admin123"},
    {"id": 2, "username": "user", "password": "password"}
]

@app.route("/")
def home():
    return "API is running"

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    for user in users:
        if user["username"] == data["username"] and user["password"] == data["password"]:
            return jsonify({"message": "Login successful"})

    return jsonify({"message": "Invalid credentials"}), 401

@app.route("/profile/<int:user_id>", methods=["GET"])
def profile(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)

    return jsonify({"message":"User not found"})
orders = [
    {"order_id":1, "user_id":1, "item":"Laptop"},
    {"order_id":2, "user_id":2, "item":"Phone"}
]

@app.route("/orders/<int:user_id>", methods=["GET"])
def get_orders(user_id):
    user_orders = [o for o in orders if o["user_id"] == user_id]
    return jsonify(user_orders)    

if __name__ == "__main__":
    app.run(debug=True)