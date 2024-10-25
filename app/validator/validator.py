from typing import Tuple
from typing import Union
import re
import datetime

from app.database.models.GenderEnum import GenderEnum

class Validator:
    # GLOBAL METHODS
    @staticmethod
    def is_empty(var: str) -> bool:
        """
        Check if the variable is an empty string

        Parameters:
            var (str): The variable to be tested

        Returns:
            (bool): True if is empty, False otherwise
        """
        return not var


    #SPECIFIC METHODS
    @staticmethod
    def first_name(first_name: str) -> Tuple[Union[bool, str]]:
        """
        Validate the first_name field

        Parameters:
            first_name (str): The user's first_name

        Returns:
            (bool, str): The success status and a message if the checks fail
        """
        if Validator.is_empty(first_name):
            return False, "O nome próprio é obrigatório."

        return True, ""


    @staticmethod
    def last_name(last_name: str) -> Tuple[Union[bool, str]]:
        """
        Validate the last_name field

        Parameters:
            last_name (str): The user's last_name

        Returns:
            (bool, str): The success status and a message if the checks fail
        """
        if Validator.is_empty(last_name):
            return False, "O apelido é obrigatório."

        return True, ""


    @staticmethod
    def username(username: str) -> Tuple[Union[bool, str]]:
        """
        Validate the username field

        Parameters:
            username (str): The user's username

        Returns:
            (bool, str): The success status and a message if the checks fail
        """
        if Validator.is_empty(username):
            return False, "O nome de utilizador é obrigatório."

        return True, ""


    @staticmethod
    def email(email: str) -> Tuple[Union[bool, str]]:
        """
        Validate the email field

        Parameters:
            email (str): The user's email

        Returns:
            (bool, str): The success status and a message if the checks fail
        """
        if Validator.is_empty(email):
            return False, "O email é obrigatório."

        if not re.match(r'\S+@\S+\.\S+', email):
            return False, "O formato de email é inválido."

        return True, ""


    @staticmethod
    def date(date: str) -> Tuple[Union[bool, str]]:
        """
        Validate the date field

        Parameters:
            date (str): The user's date

        Returns:
            (bool, str): The success status and a message if the checks fail
        """
        if Validator.is_empty(date):
            return False, "A data é obrigatória."

        if not re.match(r'\d{4}-\d{2}-\d{2}', date):
            return False, 'A data tem o formato errado. Formato correto: yyyy-mm-dd.'

        try:
            datetime.date.fromisoformat(date)
            return True, ""
        except ValueError:
            return False, 'Essa data é inválida. Formato correto: yyyy-mm-dd.'


    @staticmethod
    def gender(gender: str) -> Tuple[Union[bool, str]]:
        """
        Validate the gender field

        Parameters:
            gender (str): The user's gender

        Returns:
            (bool, str): The success status and a message if the checks fail
        """
        if Validator.is_empty(gender):
            return False, "O género é obrigatório."

        if gender not in [g.value for g in GenderEnum]:
            return False, "O género é inválido."

        return True, ""


    @staticmethod
    def password(password: str) -> Tuple[Union[bool, str]]:
        """
        Validate the password field

        Parameters:
            password (str): The user's password

        Returns:
            (bool, str): The success status and a message if the checks fail
        """
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