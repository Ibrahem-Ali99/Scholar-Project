# config.py
import pymysql

MYSQL_HOST = 'localhost'
MYSQL_USER = 'scholaradmin'
MYSQL_PASSWORD = 'scholarSWE0'
MYSQL_DB = 'scholar'
JWT_SECRET_KEY = 'your_secret_key'

try:
    connection = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
finally:
    if 'connection' in locals():
        connection.close()