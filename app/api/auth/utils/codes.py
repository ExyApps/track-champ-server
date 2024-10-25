import random
import secrets
import string

def generate_digit_code(length: int) -> str:
	"""
	Generates a x-digit code.

	Parameters:
		length (int): The length of the code

	Returns:
		(str): The code with size length
	"""
	return ''.join(str(secrets.choice(range(10))) for i in range(length))


def generate_session_cookie() -> str:
	"""
	Generates a session cookie with random lowercase letters and digits.

	Returns:
		(str): The session cookie
	"""
	return secrets.token_hex(16)