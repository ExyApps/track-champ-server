from flask import request, jsonify, g
from http import HTTPStatus

from src.database.wrapper.teams import get_team_by_id
from src.database.wrapper.teams import user_is_in_team
from src.database.wrapper.teams import add_user_to_team

from src.database.wrapper.authentication import get_user

from . import team_bp

@team_bp.route('/enter/<int:id>', methods=['POST'])
def enter(id):
    """
    Enter a public team
    """
    if not g.user_id:
        return {'success': False, 'detail': 'Não tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT
    
    team = get_team_by_id(id)

    if not team.public:
        return { 'success': False, 'detail': 'Não podes entrar nesta equipa'}, HTTPStatus.FORBIDDEN
    
    if user_is_in_team(g.user_id, id):
        return { 'success': False, 'detail': 'Já pertences a esta equipa'}, HTTPStatus.CONFLICT
    
    add_user_to_team(g.user_id, id)

    return jsonify({
        'success': True,
    }), HTTPStatus.OK