from flask import Blueprint

test_bp = Blueprint('test', __name__)

from .upload import *
from .categories import *
