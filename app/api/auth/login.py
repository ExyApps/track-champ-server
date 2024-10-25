from . import auth_bp
from flask import request, jsonify
from http import HTTPStatus

from app.api.auth.utils.security import encrypt_password
from app.database.wrapper import authentication

@auth_bp.route('/login', methods=['POST'])
def login():
	"""
	Performs the login into the system
	"""
	payload = request.json

	account_exists = authentication.account_exists(payload['email'])

	if not account_exists:
		return jsonify({ 'error': 'Essa combinação de email/password não existe', 'field': 'email' }), HTTPStatus.UNAUTHORIZED

	salt = authentication.get_salt(payload['email'])
	password, _ = encrypt_password(payload['password'], salt)

	user = authentication.login(payload['email'], password)
	
	if user is None:
		return jsonify({ 'error': 'Essa combinação de email/password não existe', 'field': 'email' }), HTTPStatus.UNAUTHORIZED
	
	authentication.update_last_login(user)
	
	info = user.to_json()

	return jsonify({
		'success': True,
		'info': info
	}), HTTPStatus.OK