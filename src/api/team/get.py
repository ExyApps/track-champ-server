from flask import request, jsonify, g
from http import HTTPStatus

from src.database.wrapper.teams import get_user_teams
from src.database.wrapper.teams import get_team_by_id
from src.database.wrapper.teams import get_team_member_count
from src.database.wrapper.teams import get_public_teams

from . import team_bp

@team_bp.route('/get-teams', methods=['GET'])
def get_teams():
    """
    Gets the user's teams and a set of public ones
    """
    if not g.user_id:
        return {'success': False, 'detail': 'Não tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT

    user_teams_objs = get_user_teams(g.user_id)
    user_teams_ids = [t.id for t in user_teams_objs]

    user_teams = [
        team.to_json() | {'members': get_team_member_count(team.id)}
        for team in user_teams_objs
    ]

    public_teams = [
        team.to_json() | {'members': get_team_member_count(team.id)}
        for team in get_public_teams(ignore_ids = user_teams_ids)
    ]

    return jsonify({'success': True, 'user_teams': user_teams, 'public_teams': public_teams}), HTTPStatus.OK