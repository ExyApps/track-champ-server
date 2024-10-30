import pytest
import datetime

from tests._fixtures.input_fields import username
from tests._fixtures.input_fields import first_name
from tests._fixtures.input_fields import last_name

from app.database.models.Users import Users
from app.database.models.GenderEnum import GenderEnum

@pytest.fixture
def user_model():
    return Users(
        username='johndoe',
        first_name='John',
        last_name='Doe',
        email='johndoe@gmail.com',
        password='Password1!',
        salt='somesalt',
        birthday='2000-01-01',
        gender=GenderEnum.MALE,
        created_in=datetime.datetime.now(),
    )