from flask import Flask, jsonify

app = Flask(__name__)

# Example route
@app.route('/api', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

if __name__ == '__main__':
    app.run(debug=True)

from flask_cors import CORS
app = Flask(__name__)
CORS(app)