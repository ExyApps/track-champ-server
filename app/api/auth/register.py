from . import auth_bp
import re
from datetime import datetime
from flask import request, jsonify
from http import HTTPStatus

from app.api.auth.utils.security import encrypt_password
from app.api.auth.utils.codes import generate_digit_code

from app.database.models.GenderEnum import match_gender
from app.database.wrapper import authentication
from app.validator.validator import Validator

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
	payload = request.json

	for k, v in payload.items():
		snake_case_key = re.sub(r'(?<!^)(?=[A-Z])', '_', k).lower()
		verifier = getattr(Validator, snake_case_key)
		valid, message = verifier(v)

		if not valid:
			return { 'error': message, 'field': k }, HTTPStatus.BAD_REQUEST

	password, salt = encrypt_password(payload['password'])

	if (authentication.account_exists(payload['email'])):
		return jsonify({ 'error': 'Este email já tem uma conta associada.', 'field': 'email' }), HTTPStatus.CONFLICT
	
	authentication.create_new_user(
		username=generate_username(payload['firstName'], payload['lastName']),
		first_name=payload['firstName'].strip(),
		last_name=payload['lastName'].strip(),
		email=payload['email'].strip(),
		password=password,
		salt=salt,
		birthday=datetime.strptime(payload['date'], '%Y-%M-%d').date(),
		gender=match_gender(payload['gender'])
	)
	
	return jsonify({ 'success': True }), HTTPStatus.CREATED