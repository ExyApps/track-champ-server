import pytest
from datetime import datetime

from app.database.models.Users import Users
from app.database.models.GenderEnum import GenderEnum

from werkzeug.security import generate_password_hash

@pytest.fixture
def user_model(username, first_name, last_name, email, date, password):
    return Users(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=generate_password_hash(password),
        birthday=datetime.strptime(date, '%Y-%m-%d'),
        gender=GenderEnum.MALE,
    )