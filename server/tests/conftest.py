import pytest
import sys
import os
from sqlalchemy.orm import scoped_session, sessionmaker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from server.app import create_app
from utils.db import db


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:", 
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "MAIL_SUPPRESS_SEND": True,
        "SESSION_TYPE": "filesystem",
    })
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def test_session(app):
    """
    created a separate session for testing to avoid affecting the original db
    """
    connection = db.engine.connect()
    transaction = connection.begin()
    options = dict(bind=connection, binds={})
    test_session_factory = sessionmaker(**options)
    test_session = scoped_session(test_session_factory)
    db.session = test_session

    yield test_session

    test_session.remove()
    transaction.rollback() 
    connection.close()


@pytest.fixture
def unique_test_data():
    from datetime import datetime
    import random

    def generate_unique_email():
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        random_suffix = random.randint(1000, 9999)
        return f"test_{timestamp}_{random_suffix}@example.com"

    return {
        "generate_unique_email": generate_unique_email,
    }
