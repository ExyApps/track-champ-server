from datetime import datetime
from flask import request, jsonify, g
from http import HTTPStatus

from src.api.auth.utils.codes import generate_digit_code

from src.database.enums.GenderEnum import match_gender
from src.database.wrapper import authentication

from werkzeug.security import generate_password_hash

from . import auth_bp

def generate_username(first_name: str, last_name: str) -> str:
    """
    Generates a username from the first and last name
    """
    username = None

    while username is None or authentication.username_exists(username):
        username = first_name.lower() + last_name.lower() + generate_digit_code(4)

    return username


@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Performs the registration into the app
    """
    if g.user_id:
        return {'success': True, 'detail': 'Já tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT

    payload = request.json

    if (authentication.account_exists(payload['email'])):
        return jsonify({ 'error': 'Este email já tem uma conta associada.', 'field': 'email' }), HTTPStatus.CONFLICT
    
    password = generate_password_hash(payload['password'])

    authentication.create_new_user(
        username=generate_username(payload['first_name'], payload['last_name']),
        first_name=payload['first_name'].strip(),
        last_name=payload['last_name'].strip(),
        email=payload['email'].strip(),
        password=password,
        birthday=datetime.strptime(payload['date'], '%Y-%m-%d').date(),
        gender=match_gender(payload['gender'])
    )

    return jsonify({ 'success': True }), HTTPStatus.CREATED
