from flask import request, jsonify, g
from http import HTTPStatus

from src.database.wrapper.teams import user_is_in_team
from src.database.wrapper.teams import get_team_by_id
from src.database.wrapper.teams import get_team_users
from src.database.wrapper.teams import get_team_admins

from src.database.wrapper.authentication import get_user

from . import team_bp

@team_bp.route('/get/<int:id>', methods=['GET'])
def get(id):
    """
    Gets the user's teams and a set of public ones
    """
    if not g.user_id:
        return {'success': False, 'detail': 'Não tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT
    
    if not user_is_in_team(g.user_id, id):
        return { 'success': False, 'detail': 'Não tens acesso a este recurso'}, HTTPStatus.FORBIDDEN
    
    team = get_team_by_id(id).to_json()
    members_objs = get_team_users(id)

    members = []
    for m in members_objs:
        members.append(
            get_user(m.user_id).to_json() | {'is_admin': m.is_admin, 'is_creator': m.is_creator}
        )

    members.sort(key=lambda m: (m['is_creator'], m['is_admin'], f"{m['first_name']} {m['last_name']}"))

    return jsonify({
        'success': True,
        'info': {
            'team': team,
            'users': members,
            'admin_ids': get_team_admins(id)
        }
    }), HTTPStatus.OK