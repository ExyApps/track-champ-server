from flask import request, jsonify, g
from http import HTTPStatus

from src.database.wrapper.teams import create_team
from src.database.wrapper.teams import add_user_to_team

from . import team_bp

@team_bp.route('/create', methods=['POST'])
def create():
    """
    Creates a team in the database
    """
    if not g.user_id:
        return {'success': False, 'detail': 'Não tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT

    payload = request.json

    team = create_team(payload['name'], payload['description'], payload['public'], payload.get('profile_image', None))
    
    add_user_to_team(g.user_id, team.id, is_admin=True, is_creator=True)

    return jsonify({'success': True, 'team': team.to_json()}), HTTPStatus.CREATED