from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from . import session_token
from . import team
from . import team_user
from . import user
from .test_category import TestCategory
from .test_event import TestEvent

from .tests.race_test import RaceTest