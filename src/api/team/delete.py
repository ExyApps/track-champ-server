from flask import jsonify, g
from http import HTTPStatus

from src.database.wrapper.teams import delete_team
from src.database.wrapper.teams import delete_team_users
from src.database.wrapper.teams import team_exists

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
    if not g.user_id:
        return {'success': False, 'detail': 'Não tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT
    
    if not team_exists(id):
        return jsonify({'success': False, 'detail': 'A equipa não existe.'}), HTTPStatus.NOT_FOUND

    delete_team(id)
    delete_team_users(id)

    return jsonify({'success': True}), HTTPStatus.OK