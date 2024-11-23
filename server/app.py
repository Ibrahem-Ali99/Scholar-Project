from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from routes.auth import auth

app = Flask(__name__)

app.register_blueprint(auth, url_prefix='/auth')
# Example route
@app.route('/api', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

if __name__ == '__main__':
    app.run(debug=True)

from flask_cors import CORS
app = Flask(__name__)
CORS(app)