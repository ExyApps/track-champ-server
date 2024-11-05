from flask import Blueprint

team_bp = Blueprint('team', __name__)

from .create import *
from .delete import *
from .update import *
