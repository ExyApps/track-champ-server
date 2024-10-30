from flask import request, jsonify
from http import HTTPStatus

from app.database.wrapper.teams import update_team
from app.database.wrapper.teams import team_exists

from app.validator.validator import Validator

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
    payload = request.json

    validation_errors = Validator.validate_payload(payload)
    if validation_errors:
        return {'success': False, 'errors': validation_errors}, HTTPStatus.BAD_REQUEST
    
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