from flask import Blueprint

team_bp = Blueprint('team', __name__)

from .create import *
from .get import *
from .get_teams import *
from .delete import *
from .update import *
