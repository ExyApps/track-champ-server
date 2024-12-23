import os
from datetime import datetime
from flask import request, jsonify, g, make_response
from http import HTTPStatus

from src.api.auth.utils.codes import generate_session_cookie
from src.database.wrapper import authentication

from werkzeug.security import check_password_hash

from . import auth_bp

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Performs the login into the system
    """
    if g.user_id:
        return {'success': True, 'detail': 'Já tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT

    payload = request.json

    user = authentication.get_account_by_email(payload['email'])

    if not user:
        return jsonify({ 'error': 'Essa combinação de email/password não existe', 'field': 'email' }), HTTPStatus.UNAUTHORIZED

    if not check_password_hash(user.password, payload['password']):
        return jsonify({ 'error': 'Essa combinação de email/password não existe', 'field': 'email' }), HTTPStatus.UNAUTHORIZED

    session_token = generate_session_cookie()
    authentication.store_session_token(user.id, session_token)

    info = user.to_json()

    response = make_response({
        'success': True,
        'info': info
    })
    response.set_cookie(
        'session_token',
        session_token,
        path='/',
        expires=datetime.fromisocalendar(2026, 2, 1),
        httponly=True,
        secure='localhost' not in os.getenv('WEBSITE_URL'),
        samesite='None' if 'localhost' not in os.getenv('WEBSITE_URL') else None
    )

    return response, HTTPStatus.OK
