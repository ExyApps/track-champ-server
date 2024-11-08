from flask import request, jsonify, g
from http import HTTPStatus

from src.database.wrapper.teams import user_is_in_team
from src.database.wrapper.teams import promote_team_member

from . import team_bp

@team_bp.route('/promote', methods=['POST'])
def promote():
    """
    Promote a user in the team
    """
    if not g.user_id:
        return {'success': False, 'detail': 'Não tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT

    payload = request.json

    user_id = payload['user_id']
    team_id = payload['team_id']

    if not user_is_in_team(user_id, team_id):
        return { 'success': False, 'detail': 'Não foi encontrada uma correspondência.'}, HTTPStatus.CONFLICT

    promote_team_member(user_id, team_id)

    return jsonify({'success': True}), HTTPStatus.OK