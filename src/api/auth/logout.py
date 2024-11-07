import os
from datetime import datetime
from flask import request, jsonify, g, make_response
from http import HTTPStatus

from src.database.wrapper import authentication

from . import auth_bp

@auth_bp.route('/logout', methods=['POST'])
def logout():
    """
    Performs the login into the system
    """
    if not g.user_id:
        return {'success': False, 'detail': 'Não tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT

    authentication.delete_session_token(g.user_id, g.session_token)

    response = make_response({'success': True})
    response.set_cookie(
        'session_token',
        '',
        path='/',
        expires=0,
        httponly=True,
        secure='localhost' not in os.getenv('WEBSITE_URL'),
        samesite='None' if 'localhost' not in os.getenv('WEBSITE_URL') else None
    )

    return response, HTTPStatus.OK
