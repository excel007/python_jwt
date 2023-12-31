#follow this file https://flask-jwt-extended.readthedocs.io/en/stable/basic_usage.html
from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)

#Setup the Flask-JWT-Extension
app.config["JWT_SECRET_KEY"] = "123456"
jwt = JWTManager(app)

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login",methods=["POST"])
def login():
    username = request.json.get("username",None)
    password = request.json.get("password",None)
    if username != "test" or password != "test":
        return jsonify(msg="username or password is missing")
    
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token),401

# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/protected",methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as='current_user'),200

if __name__ == "__main__":
    app.run(debug=True)

