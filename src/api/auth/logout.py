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
    response.set_cookie('session_token', '', expires=0, path='/', httponly=True, samesite='Lax')
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000' # or your React app's origin
    response.headers['Access-Control-Allow-Credentials'] = 'true' # crucial for cookies

    return response, HTTPStatus.OK
