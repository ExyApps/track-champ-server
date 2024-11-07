from flask import request, jsonify, g
from http import HTTPStatus

from src.database.wrapper.teams import user_is_in_team
from src.database.wrapper.teams import exit_team

from . import team_bp

@team_bp.route('/exit/<int:id>', methods=['POST'])
def exit(id):
    """
    Exit a team
    """
    if not g.user_id:
        return {'success': False, 'detail': 'Não tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT
    
    if not user_is_in_team(g.user_id, id):
        return { 'success': False, 'detail': 'Não pertences a esta equipa'}, HTTPStatus.CONFLICT
    
    exit_team(g.user_id, id)

    return jsonify({
        'success': True,
    }), HTTPStatus.OK