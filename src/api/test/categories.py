from flask import request, jsonify, g
from http import HTTPStatus

from src.database.wrapper.tests import get_categories
from src.database.wrapper.tests import get_category_tests

from . import test_bp

@test_bp.route('/categories', methods=['GET'])
def categories():
    """
    Get all the test categories the app has
    """
    if not g.user_id:
        return {'success': False, 'detail': 'Não tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT

    categories = [c.to_json() for c in get_categories()]
    for c in categories:
        c['tests'] = [t.to_json('category') for t in get_category_tests(c['id'])]

    return {'success': True, 'categories': categories}, HTTPStatus.OK