from flask import Blueprint

team_bp = Blueprint('team', __name__)

from .create import *
from .enter import *
from .exit import *
from .get import *
from .get_teams import *
from .invite import *
from .delete import *
from .update import *
from .promote import *
from .depromote import *
