from typing import Tuple
from typing import Union
import re

from app.database.models.GenderEnum import GenderEnum, match_gender

class Validator:
	# GLOBAL METHODS
	@staticmethod
	def is_empty(var: str) -> bool:
		return not var
	

	#SPECIFIC METHODS
	@staticmethod
	def first_name(first_name: str) -> Tuple[Union[bool, str]]:
		if Validator.is_empty(first_name):
			return False, "O nome próprio é obrigatório."

		return True, ""


	@staticmethod
	def last_name(last_name: str) -> Tuple[Union[bool, str]]:
		if Validator.is_empty(last_name):
			return False, "O apelido é obrigatório."

		return True, ""	
	

	@staticmethod
	def username(username: str) -> Tuple[Union[bool, str]]:
		if Validator.is_empty(username):
			return False, "O nome de utilizador é obrigatório."
		
		return True, ""
	

	@staticmethod
	def email(email: str) -> Tuple[Union[bool, str]]:
		if Validator.is_empty(email):
			return False, "O email é obrigatório."
		
		if not re.match(r'\S+@\S+\.\S+', email):
			return False, "O formato de email é inválido."
		
		return True, ""
	

	@staticmethod
	def date(date: str) -> Tuple[Union[bool, str]]:
		if Validator.is_empty(date):
			return False, "A data é obrigatória."

		return True, ""


	@staticmethod
	def gender(gender: str) -> Tuple[Union[bool, str]]:
		if Validator.is_empty(gender):
			return False, "O género é obrigatório."

		if gender not in [g.value for g in GenderEnum]:
			return False, "O género é inválido."

		return True, ""
		
	
	@staticmethod
	def password(password: str) -> Tuple[Union[bool, str]]:
		if Validator.is_empty(password):
			return False, "A password é obrigatória."

		if len(password) < 8:
			return False, "A password deve ter pelo menos 8 caracteres."
	
		if password == password.lower():
			return False, "A password tem de ter pelo menos 1 letra maiúscula."
	
		if password == password.upper():
			return False, "A password tem de ter pelo menos 1 letra minúscula."
		
		if not re.search(r'\d', password):
			return False, "A password tem de ter pelo menos 1 número."
	
		if not re.search(r'[ `!@#$%^&*()_+\-=[\]{};\':"\\|,.<>/?~]', password):
			return False, "A password tem de ter pelo menos 1 caracter especial."

		return True, ""