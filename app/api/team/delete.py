from flask import request, jsonify
from http import HTTPStatus

from app.database.wrapper.teams import delete_team

from app.validator.validator import Validator

from . import team_bp

@team_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id: int):
    """
    Deletes a team in the database

    Parameters
    ----------
        id: int
            The team's id
    """
    delete_team(id)

    return jsonify({'success': True}), HTTPStatus.OK