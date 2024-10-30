import re
import datetime
from typing import *

from app.database.models.GenderEnum import GenderEnum

IGNORED_FIELDS = ['id', 'profile_image']

class Validator:
    @staticmethod
    def validate_payload(payload: Dict[str, Union[str, int]]) -> List[Tuple[Union[bool, str]]]:
        """
        General function that validates the payload received

        Parameters
        ----------
            payload: Dict[str, Union[str, int]]
                Information send with the request

        Returns
        -------
            List[Tuple[Union[bool, str]]]
                A list of errors and respective fields
        """
        validation_errors = []

        for k, v in payload.items():
            if k in IGNORED_FIELDS:
                continue

            # Make type verifications
            type_validator = f'_validate_{type(v).__name__}'
            verifier = getattr(Validator, type_validator)
            valid, message = verifier(v)

            if not valid:
                validation_errors.append({ 'field': k, 'error': message })
                continue

            # Make field specific verifications
            verifier = getattr(Validator, f'_validate_{k}', lambda _: (True, ''))
            valid, message = verifier(v)

            if not valid:
                validation_errors.append({ 'field': k, 'error': message })

        return validation_errors
    

    # GLOBAL CHECKS
    @staticmethod
    def _is_empty(var: str) -> bool:
        """
        Check if the variable is an empty string

        Parameters
        ----------
            var: str
                The variable to be tested

        Returns
        -------
            bool
                True if is empty, False otherwise
        """
        return not var
    

    # TYPE CHECKS
    @staticmethod
    def _validate_str(var: str) -> Tuple[Union[bool, str]]:
        """
        General function that validates the common elements of a string argument

        Parameters
        ----------
            var: str
                The value sent in the payload

        Returns
        -------
            Tuple[Union[bool, str]]
                The success status and a message if the checks fail
        """
        if Validator._is_empty(var):
            return False, "Este campo é obrigatório."
        
        return True, ''
    

    def _validate_bool(var: bool) -> Tuple[Union[bool, str]]:
        """
        General function that validates the common elements of a string argument

        Parameters
        ----------
            var: str
                The value sent in the payload

        Returns
        -------
            Tuple[Union[bool, str]]
                The success status and a message if the checks fail
        """
        return True, ''
    

    #SPECIFIC METHODS
    @staticmethod
    def _validate_email(email: str) -> Tuple[Union[bool, str]]:
        """
        Validate the email field

        Parameters
        ----------
            email: str
                The user's email

        Returns
        -------
            Tuple[Union[bool, str]]
                The success status and a message if the checks fail
        """
        if not re.match(r'\S+@\S+\.\S+', email):
            return False, "Formato inválido."

        return True, ""


    @staticmethod
    def _validate_date(date: str) -> Tuple[Union[bool, str]]:
        """
        Validate the date field

        Parameters
        ----------
            date: str
                The user's date

        Returns
        -------
            Tuple[Union[bool, str]]
                The success status and a message if the checks fail
        """
        if not re.match(r'\d{4}-\d{2}-\d{2}', date):
            return False, 'Formato errado. Formato correto: yyyy-mm-dd.'

        try:
            datetime.date.fromisoformat(date)
            return True, ""
        except ValueError:
            return False, 'Formato errado. Formato correto: yyyy-mm-dd.'


    @staticmethod
    def _validate_gender(gender: str) -> Tuple[Union[bool, str]]:
        """
        Validate the gender field

        Parameters
        ----------
            gender: str
                The user's gender

        Returns
        -------
            Tuple[Union[bool, str]]
                The success status and a message if the checks fail
        """
        if gender not in [g.value for g in GenderEnum]:
            return False, "Género inválido."

        return True, ""


    @staticmethod
    def _validate_password(password: str) -> Tuple[Union[bool, str]]:
        """
        Validate the password field

        Parameters
        ----------
            password: str
                The user's password

        Returns
        -------
            Tuple[Union[bool, str]]
                The success status and a message if the checks fail
        """
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