from flask import Flask, jsonify
from dotenv import load_dotenv
from extensions import init_extensions
from flask_cors import CORS
import logging


logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s',  
    handlers=[
        logging.FileHandler("app.log"),  
        logging.StreamHandler()         
    ]
)


# Load environment variables
load_dotenv()

app = Flask(__name__)

# Secret Key for Session Management
app.secret_key = "default_secret_key"

# Flask Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'

app.config['GOOGLE_CLIENT_ID'] = "your_google_client_id"
app.config['GOOGLE_CLIENT_SECRET'] = "your_google_client_secret"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'

# Initialize all extensions
init_extensions(app)

# Configure CORS 
CORS(app, origins=["http://localhost:5173"], supports_credentials=True)

from routes.auth import auth  

# Register Blueprints
app.register_blueprint(auth, url_prefix='/auth')

@app.route('/api', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

if __name__ == '__main__':
    app.run(debug=True)