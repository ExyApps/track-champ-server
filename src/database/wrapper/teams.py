from typing import List, Optional

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


def get_user_teams(id: int) -> List[Team]:
    """
    Retrieve a list of teams that the user is in

    Parameters
    ----------
        id: int
            The user's id
    """
    tus = TeamUser.query.filter_by(user_id = id).all()
    return [get_team_by_id(t.team_id) for t in tus]


def get_public_teams(search: str = '', offset: int = 0, limit: int = 10, ignore_ids = []) -> List[Team]:
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
            (
                Team.public & (
                    Team.name.ilike(f'%{search}%') | Team.description.ilike(f'%{search}%')
                ) & (
                    ~Team.id.in_(ignore_ids)
                )
            )
        )
        .order_by(Team.name)
        .offset(offset)
        .limit(limit)
        .all()
    )
    return teams
    

def get_team_by_id(id: int) -> Optional[Team]:
    """
    Get a team by its id

    Parameters
    ----------
        id: int
            The team's id

    Returns
    -------
        Optional[Team]
            The team object
    """
    return Team.query.get(id)


def get_team_member_count(id: int) -> int:
    """
    Get the team member count

    Parameters
    ----------
        id: int
            The team's id

    Returns
    -------
        int
            The number of members in the group
    """
    return TeamUser.query.filter_by(team_id=id).count()


def get_team_users(id: int) -> List[TeamUser]:
    """
    Get a list of the team users that are on a team

    Parameters
    ----------
        id: int
            The team's id

    Returns
    -------
        List[TeamUser]
            A list of all the team users
    """
    return TeamUser.query.filter_by(team_id=id).all()


def user_is_creator(user_id: int, team_id: int) -> bool:
    """
    Check if a user is the creator of the team

    Parameters
    ----------
        user_id: int
            The user's id

        team_id: int
            The team's id

    Returns
    -------
        bool
            If the user is the creator or not
    """
    tu = TeamUser.query.filter_by(user_id=user_id, team_id=team_id).first()

    if not tu:
        return False
    
    return tu.is_creator


def get_team_admins(id: int) -> List[int]:
    """
    Get a list of the users' id that are admins in a team

    Parameters
    ----------
        id: int
            The team's id

    Returns
    -------
        List[int]
            A list of all the users' ids
    """
    ids = [tu.user_id for tu in TeamUser.query.filter_by(team_id=id).all() if tu.is_admin]
    return ids
    

def add_user_to_team(user_id: int, team_id: int, is_admin: bool = False, is_creator: bool = False) -> None:
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
        is_admin = is_admin,
        is_creator = is_creator
    )

    db = app.extensions['sqlalchemy']
    db.session.add(tu)
    db.session.commit()


def exit_team(user_id: int, team_id: int) -> None:
    """
    Remove a user from a team

    Parameters
    ----------
        user_id: int
            The user's id

        team_id: int
            The team's id
    """
    tu = TeamUser.query.filter_by(user_id=user_id, team_id=team_id).first()

    db = app.extensions['sqlalchemy']
    db.session.delete(tu)
    db.session.commit()


def user_is_in_team(user_id: int, team_id: int) -> bool:
    """
    Checks if a user has is in a team

    Parameters
    ----------
        user_id: int
            The user's id

        team_id: int
            The team's id

    Returns
    -------
        bool
            If the user is or not in a team
    """
    return TeamUser.query.filter_by(user_id=user_id, team_id=team_id).first() is not None


def user_can_see_team_details(user_id: int, team_id: int) -> bool:
    """
    Checks if a user has access to a team's details

    Parameters
    ----------
        user_id: int
            The user's id

        team_id: int
            The team's id

    Returns
    -------
        bool
            If the user has access or not to the team's details
    """
    return Team.query.filter_by(id=team_id).first().public or user_is_in_team(user_id, team_id)


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