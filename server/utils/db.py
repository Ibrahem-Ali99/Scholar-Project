from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    """
    Initialize the SQLAlchemy database with the Flask app.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{app.config['MYSQL_USER']}:{app.config['MYSQL_PASSWORD']}"
        f"@{app.config['MYSQL_HOST']}/{app.config['MYSQL_DB']}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
