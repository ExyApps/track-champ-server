from typing import List

from flask import current_app as app

from src.database.models.team import Team
from src.database.models.team_user import TeamUser


def create_team(name: str, description: str, public: bool, profile_image: str) -> Team:
    """
    Create a new team and insert it into the database

    Parameters
    ----------
        name: str
            The team's name

        description: str
            The team's description

        public: bool
            If the team is acessible to everyone or not

        profile_image: str
            The team's profile image
    """
    team = Team(
        name = name,
        description = description,
        public = public,
        profile_image = profile_image
    )

    db = app.extensions['sqlalchemy']
    db.session.add(team)
    db.session.commit()
    db.session.refresh(team)
    return team


def delete_team(id: int) -> None:
    """
    Delete a team from the database

    Parameters:
        id (int): The team's id
    """
    team = Team.query.get(id)

    db = app.extensions['sqlalchemy']
    db.session.delete(team)
    db.session.commit()


def update_team(id: int, name: int, description: int, public: bool, profile_image: str) -> Team:
    """
    Updates the team details

    Parameters:
        id (int): The team's id
        name (str): The team's name
        description (str): The team's description
        public (bool): If the team is acessible to everyone or not
        profile_image (str): The team's profile image
    """
    team = Team.query.get(id)
    team.name = name
    team.description = description
    team.public = public
    team.profile_image = profile_image

    db = app.extensions['sqlalchemy']
    db.session.commit()
    db.session.refresh(team)
    return team


def get_public_teams(search: str = '', offset: int = 0, limit: int = 10) -> List[Team]:
    """
    Retrieve a list of public teams

    Parameters:
        search (str): Input to be searched in the name or description
        offset (int): The number of results to be skipped
        limit (int): The number of results to be returned

    Returns:
        (List[Team]): A list of teams that match the criteria
    """
    teams = (
        Team.query.filter(
            (Team.public & (Team.name.ilike(f'%{search}%') | Team.description.ilike(f'%{search}%')))
        )
        .order_by(Team.name)
        .offset(offset)
        .limit(limit)
        .all()
    )
    return teams
    

def team_exists(id: int) -> bool:
    """
    Check if a team exists

    Parameters
    ----------
        id: int
            The team's id

    Returns
    -------
        bool
            True if the team exists, False otherwise
    """
    return Team.query.get(id) is not None
    

def get_team_users(id: int) -> List[int]:
    """
    Get a list of the users' id that are in a team

    Parameters
    ----------
        id: int
            The team's id

    Returns
    -------
        List[int]
            A list of all the users' ids
    """
    ids = [tu.user_id for tu in TeamUser.query.filter_by(team_id=id).all()]
    return ids
    

def add_user_to_team(user_id: int, team_id: int, is_admin: bool = False) -> None:
    """
    Adds a user to a team

    Parameters
    ----------
        user_id: int
            The user's id

        team_id: int
            The team's id

        is_admin: bool
            If the user should be an admin or not
    """
    tu = TeamUser(
        user_id = user_id,
        team_id = team_id,
        is_admin = is_admin
    )

    db = app.extensions['sqlalchemy']
    db.session.add(tu)
    db.session.commit()


def delete_team_users(id: int) -> None:
    """
    Delete all the rows with the team's id

    Parameters
    ----------
        id: int
            The team's id
    """
    rows = TeamUser.query.filter_by(team_id = id).all()

    db = app.extensions['sqlalchemy']
    for row in rows:
        db.session.delete(row)
    db.session.commit()