from flask import request, jsonify
from http import HTTPStatus

from app.database.wrapper.teams import delete_team
from app.database.wrapper.teams import team_exists

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
    if not team_exists(id):
        return jsonify({'success': False, 'detail': 'A equipa não existe.'}), HTTPStatus.NOT_FOUND

    delete_team(id)

    return jsonify({'success': True}), HTTPStatus.OK