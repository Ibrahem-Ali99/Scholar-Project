import os
from dotenv import load_dotenv
from datetime import timedelta
import pymysql

# Load environment variables from .env file
load_dotenv()

# Session Config
SECRET_KEY = os.getenv("APP_SECRET_KEY", "default_secret_key")  
SESSION_COOKIE_NAME = os.getenv("SESSION_COOKIE_NAME", "google-login-session")
PERMANENT_SESSION_LIFETIME = timedelta(minutes=int(os.getenv("SESSION_LIFETIME", 10)))  
SESSION_TYPE = os.getenv("SESSION_TYPE", "filesystem") 

# SQL Configuration
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_DB = os.getenv("MYSQL_DB", "test_db")

# Test MySQL Connection
try:
    connection = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    print("MySQL connection successful!")
except Exception as e:
    print(f"Failed to connect to MySQL: {e}")
finally:
    if 'connection' in locals():
        connection.close()
        
        
# Flask-Mail Config
MAIL_SERVER = 'smtp.gmail.com'  
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.getenv("MAIL_USERNAME")  # Your email address
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")  # App-specific password or email password
MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", MAIL_USERNAME)
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")  # Your frontend's base URL