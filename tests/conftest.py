import pytest
# from app import create_app, db  # Import your app factory and db instance
# from app.database.models import User  # Example model import (adapt as needed)

# # --- Fixtures ---

# @pytest.fixture(scope="session")
# def app():
#     """Session-scoped fixture for the Flask app.  Creates the app in testing mode."""
#     app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})  # Use in-memory SQLite for testing
#     with app.app_context():
#         yield app

# @pytest.fixture(scope="session")
# def _db(app):
#     """Session-scoped fixture for the database.  Creates all tables."""
#     with app.app_context():
#         db.create_all()
#         yield db
#         db.drop_all()  # Clean up after tests