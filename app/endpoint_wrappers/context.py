from flask import Flask, request, g
from http import HTTPStatus

from app.database.wrapper.authentication import get_user_by_session_token
from app.validator.validator import Validator

def setup_context(app: Flask) -> None:
    """
    Setup the context of the endpoints

    Parameters
    ----------
        app: Flask
            The app object
    """
    @app.before_request
    def create_context():
        """
        Handle the session token to identify the user
        """
        session_token = request.cookies.get('session_token', None)

        g.session_token = session_token
        g.user_id = None

        if session_token:
            # Identify the user
            g.user_id = get_user_by_session_token(session_token)

def setup_body_verification(app: Flask) -> None:
    """
    Setup the endpoint's body validation 

    Parameters
    ----------
        app: Flask
            The app object
    """
    @app.before_request
    def body_validation():
        """
        Validate the endpoint's body
        """
        if request.is_json:
            payload = request.json

            errors = Validator.validate_payload(payload)
            if errors:
                return {'success': False, 'errors': errors}, HTTPStatus.BAD_REQUEST