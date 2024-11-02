import pytest
from datetime import datetime

from _fixtures.input_fields import username
from _fixtures.input_fields import first_name
from _fixtures.input_fields import last_name
from _fixtures.input_fields import email
from _fixtures.input_fields import date
from _fixtures.input_fields import password
from _fixtures.input_fields import salt

from app.api.auth.utils.security import encrypt_password

from app.database.models.Users import Users
from app.database.models.GenderEnum import GenderEnum

@pytest.fixture
def user_model(username, first_name, last_name, email, date, password, salt):
    print(encrypt_password(password, salt)[0])
    return Users(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=encrypt_password(password, salt)[0],
        salt=salt,
        birthday=datetime.strptime(date, '%Y-%m-%d'),
        gender=GenderEnum.MALE,
    )