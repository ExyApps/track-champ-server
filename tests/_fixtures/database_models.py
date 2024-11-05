import pytest
from datetime import datetime
from werkzeug.security import generate_password_hash

from app.database.models.user import User
from app.database.enums.GenderEnum import GenderEnum
from app.database.models.team import Team
from app.database.models.team_user import TeamUser

@pytest.fixture()
def user(username, first_name, last_name, email, date, password):
    return User(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=generate_password_hash(password),
        birthday=datetime.strptime(date, '%Y-%m-%d'),
        gender=GenderEnum.MALE,
    )


@pytest.fixture()
def team(name, description, boolean_field):
    return Team(
        name=name,
        description=description,
        public=boolean_field
    )


@pytest.fixture()
def team_user():
    return TeamUser(
        user_id=1,
        team_id=1,
        is_admin=True
    )