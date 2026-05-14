from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "arham+923362555320"
jwt = JWTManager(app)

users = {}

@app.route("/")
def home():
    return "Server is running!"

@app.route("/register", methods=["POST"])
def register():
    username = request.json.get("username")
    password = request.json.get("password")
    users[username] = password
    return jsonify({"msg": "User registered successfully"}), 201


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if users.get(username) == password:

        token = create_access_token(identity=username)
        return jsonify(access_token=token)
    return jsonify({"msg": "Bad username or password"}), 401

@app.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user, status="Welcome to your profile!")


if __name__ == "__main__":
    app.run(debug=True)

