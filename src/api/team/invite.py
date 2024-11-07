from flask import request, jsonify, g
from http import HTTPStatus

from src.database.wrapper.teams import get_team_by_id
from src.database.wrapper.teams import add_user_to_team
from src.database.wrapper.teams import user_is_creator
from src.database.wrapper.teams import get_team_admins
from src.database.wrapper.teams import get_team_by_id
from src.database.wrapper.teams import user_is_in_team

from src.database.wrapper.authentication import get_user_by_username

from . import team_bp

@team_bp.route('/invite', methods=['POST'])
def invite():
    """
    Invites a user to a team
    """
    if not g.user_id:
        return {'success': False, 'detail': 'Não tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT

    payload = request.json

    if not get_team_by_id(payload['team_id']):
        return jsonify({'success': False, 'detail': 'A equipa não existe.'}), HTTPStatus.NOT_FOUND
    
    if not user_is_creator(g.user_id, payload['team_id']) and g.user_id not in get_team_admins(payload['team_id']):
        return jsonify({'success': False, 'detail': 'Não tens permissões.'}), HTTPStatus.FORBIDDEN
    
    user = get_user_by_username(payload['username']);

    if not user:
        return jsonify({'success': False, 'detail': 'O utilizador não existe.'}), HTTPStatus.NOT_FOUND
    
    if user_is_in_team(user.id, payload['team_id']):
        return jsonify({'success': False, 'detail': 'O utilizador já esta na equipa.'}), HTTPStatus.CONFLICT
    
    add_user_to_team(user.id, payload['team_id'])

    team = get_team_by_id(payload['team_id'])

    return jsonify({'success': True, 'team': team.to_json()}), HTTPStatus.CREATED