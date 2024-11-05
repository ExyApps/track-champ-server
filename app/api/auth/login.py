from datetime import datetime
from flask import request, jsonify, g, make_response
from http import HTTPStatus

from app.api.auth.utils.codes import generate_session_cookie
from app.database.wrapper import authentication

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
    print(session_token)
    authentication.store_session_token(user.id, session_token)

    info = user.to_json()

    response = make_response({
        'success': True,
        'info': info
    })
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000' # or your React app's origin
    response.headers['Access-Control-Allow-Credentials'] = 'true' # crucial for cookies
    response.set_cookie(
        'session_token',
        session_token,
        expires=datetime.fromisocalendar(2026, 2, 1),
        httponly=True,
        samesite='Lax'
    )

    return response, HTTPStatus.OK
