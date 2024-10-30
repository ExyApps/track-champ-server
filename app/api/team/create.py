from flask import request, jsonify
from http import HTTPStatus

from app.database.wrapper.teams import create_team
from app.database.wrapper.teams import add_user_to_team

from app.validator.validator import Validator

from . import team_bp

@team_bp.route('/create', methods=['POST'])
def create():
    """
    Creates a team in the database
    """
    payload = request.json

    validation_errors = Validator.validate_payload(payload)
    if validation_errors:
        return {'success': False, 'errors': validation_errors}, HTTPStatus.BAD_REQUEST

    team = create_team(payload['name'], payload['description'], payload['public'], payload.get('profile_image', None))
    
    # TODO: User id needs to be obtained from session cookie
    add_user_to_team(0, team.id, True)

    return jsonify({'success': True, 'team': team.to_json()}), HTTPStatus.CREATED