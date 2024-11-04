import pytest

from app.initializer import create_app
from app.database.models import db
from config import TestConfig

from _fixtures.input_fields import *
from _fixtures.database_models import *
from _fixtures.payloads import *

# # --- Fixtures ---

@pytest.fixture(scope='session')
def app():
    app = create_app(config_class=TestConfig) #Use TestConfig here
    with app.app_context():
        db.create_all()
        yield app
    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='function')
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='class')
def db_session(app):
    with app.app_context():
        db.create_all()
        yield db.session
        db.session.remove()
        db.drop_all()