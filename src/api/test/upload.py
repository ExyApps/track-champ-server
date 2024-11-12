from flask import request, jsonify, g
from http import HTTPStatus

from src.database.test_match import TestMatch
from src.database.wrapper.tests import get_category_by_id
from src.database.wrapper.tests import get_test_by_id
from src.database.wrapper.tests import create_test_event

from . import test_bp

@test_bp.route('/upload', methods=['POST'])
def upload():
    """
    Upload test results to the database
    """
    if not g.user_id:
        return {'success': False, 'detail': 'Não tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT
    
    payload = request.json

    category = get_category_by_id(payload['category'])
    if not category:
        return jsonify({'success': False, 'detail': 'A categoria não existe.'}), HTTPStatus.NOT_FOUND
    
    test = get_test_by_id(payload['test'])
    if not test:
        return jsonify({'success': False, 'detail': 'O teste não existe.'}), HTTPStatus.NOT_FOUND

    test_event = create_test_event(category.id, test.id, payload['athlete'], payload.get('date', None))
    model_function = TestMatch.get_test_model(category.name, test.name)

    for result in payload['result']:
        model_function(test_event.id, result)

    return {'success': True}, HTTPStatus.CREATED