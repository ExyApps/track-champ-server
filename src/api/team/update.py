from flask import request, jsonify, g
from http import HTTPStatus

from src.database.wrapper.teams import update_team
from src.database.wrapper.teams import get_team_by_id

from . import team_bp

@team_bp.route('/update/<int:id>', methods=['PUT'])
def update(id: int):
    """
    Updates a team in the database

    Parameters
    ----------
        id: int
            The team's id
    """
    if not g.user_id:
        return {'success': False, 'detail': 'Não tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT
    
    payload = request.json
    
    if not get_team_by_id(id):
        return jsonify({'success': False, 'detail': 'A equipa não existe.'}), HTTPStatus.NOT_FOUND

    team = update_team(
        id,
        payload['name'],
        payload['description'],
        payload['public'],
        payload.get('profile_image', None)
    )

    return jsonify({'success': True, 'team': team.to_json()}), HTTPStatus.OK