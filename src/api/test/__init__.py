from flask import Blueprint

test_bp = Blueprint('test', __name__)

from .create import *
from .categories import *
