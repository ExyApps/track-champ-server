from flask import request, jsonify, g
from http import HTTPStatus

from app.database.wrapper.teams import update_team
from app.database.wrapper.teams import team_exists

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
    
    if not team_exists(id):
        return jsonify({'success': False, 'detail': 'A equipa não existe.'}), HTTPStatus.NOT_FOUND

    team = update_team(
        id,
        payload['name'],
        payload['description'],
        payload['public'],
        payload.get('profile_image', None)
    )

    return jsonify({'success': True, 'team': team.to_json()}), HTTPStatus.OK