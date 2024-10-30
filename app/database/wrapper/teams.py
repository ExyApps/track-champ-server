from typing import List

from extension import app, db

from app.database.models.Teams import Teams
from app.database.models.TeamUsers import TeamUsers


def create_team(name: str, description: str, public: bool, profile_image: str) -> Teams:
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
    with app.app_context():
        team = Teams(
            name = name,
            description = description,
            public = public,
            profile_image = profile_image
        )

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
    with app.app_context():
        team = Teams.query.get(id)
        db.session.delete(team)
        db.session.commit()


def update_team(id: int, name: int, description: int, public: bool, profile_image: str) -> Teams:
    """
    Updates the team details

    Parameters:
        id (int): The team's id
        name (str): The team's name
        description (str): The team's description
        public (bool): If the team is acessible to everyone or not
        profile_image (str): The team's profile image
    """
    with app.app_context():
        team = Teams.query.get(id)
        team.name = name
        team.description = description
        team.public = public
        team.profile_image = profile_image

        db.session.commit()
        db.session.refresh(team)
        return team


def get_public_teams(search: str = '', offset: int = 0, limit: int = 10) -> List[Teams]:
    """
    Retrieve a list of public teams

    Parameters:
        search (str): Input to be searched in the name or description
        offset (int): The number of results to be skipped
        limit (int): The number of results to be returned

    Returns:
        (List[Teams]): A list of teams that match the criteria
    """
    with app.app_context():
        teams = (
            Teams.query.filter(
                (Teams.public & (Teams.name.ilike(f'%{search}%') | Teams.description.ilike(f'%{search}%')))
            )
            .order_by(Teams.name)
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
    with app.app_context():
        return Teams.query.get(id) is not None
    

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
    with app.app_context():
        ids = [tu.user_id for tu in TeamUsers.query.filter_by(team_id=id).all()]
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
    tu = TeamUsers(
        user_id = user_id,
        team_id = team_id,
        is_admin = is_admin
    )

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
    rows = TeamUsers.query.filter_by(team_id = id).all()

    for row in rows:
        db.session.delete(row)
    db.session.commit()