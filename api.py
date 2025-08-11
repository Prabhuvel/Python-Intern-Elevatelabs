from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user store
users = [
    {"id": 1, "name": "prabhu", "email": "prabhu@gmail.com"},
    {"id": 2, "name": "Vel", "email": "vel@gamil.com"}
]

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200  

# GET single user by ID 
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:  # O(n)
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# POST - Add a new user 
@app.route("/users", methods=["POST"])
def create_user():
    new_user = request.json
    max_id = 0
    for user in users:  
        if user["id"] > max_id:
            max_id = user["id"]
    new_user["id"] = max_id + 1
    users.append(new_user)  # O(1)
    return jsonify(new_user), 201

# PUT - Update user 
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    for user in users: 
        if user["id"] == user_id:
            data = request.json
            for key in data:  
                user[key] = data[key]
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# DELETE - Remove user 
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    new_list = []
    for user in users: 
        if user["id"] != user_id:
            new_list.append(user)
    users = new_list
    return jsonify({"message": "User deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
