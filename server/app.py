from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

# Initialize Flask app
app = Flask(
    __name__,
    static_folder="../client/dist",  # Path to React build folder
    static_url_path=""
)
CORS(app)

# API Endpoint
@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Welcome to the Flask API!"})

# Serve React Frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        # Serve the requested file (e.g., JS, CSS)
        return send_from_directory(app.static_folder, path)
    else:
        # Serve the React app's index.html for all other routes
        return send_from_directory(app.static_folder, "index.html")

if __name__ == '__main__':
    app.run(debug=True)
