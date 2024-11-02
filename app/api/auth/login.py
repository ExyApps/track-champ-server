from flask import request, jsonify, g
from http import HTTPStatus

from app.api.auth.utils.security import encrypt_password
from app.api.auth.utils.codes import generate_session_cookie
from app.database.wrapper import authentication

from . import auth_bp

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Performs the login into the system
    """
    # if g.user_id:
    #     return {'success': True, 'detail': 'Já tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT

    payload = request.json

    account_exists = authentication.account_exists(payload['email'])

    if not account_exists:
        return jsonify({ 'error': 'Essa combinação de email/password não existe', 'field': 'email' }), HTTPStatus.UNAUTHORIZED

    salt = authentication.get_salt(payload['email'])
    password, _ = encrypt_password(payload['password'], salt)

    print(payload)
    print([x.to_json() for x in authentication.get_users()])

    user = authentication.login(payload['email'], password)

    if user is None:
        return jsonify({ 'error': 'Essa combinação de email/password não existe', 'field': 'email' }), HTTPStatus.UNAUTHORIZED

    session_token = generate_session_cookie()
    authentication.store_session_token(user.id, session_token)

    info = user.to_json()

    response = jsonify({
        'success': True,
        'info': info
    })
    response.set_cookie('session_token', session_token)

    return response, HTTPStatus.OK
