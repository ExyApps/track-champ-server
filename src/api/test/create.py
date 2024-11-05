from flask import request, jsonify, g
from http import HTTPStatus

from src.database.models.tests import *

from src.database.enums.TestEnum import match_test

from . import test_bp

@test_bp.route('/create', methods=['POST'])
def create():
    """
    Creates a test result in the database
    """
    if not g.user_id:
        return {'success': False, 'detail': 'Não tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT
    
    payload = request.json

    test = match_test(payload['test'])

    return {}, HTTPStatus.CREATED