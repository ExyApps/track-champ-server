from typing import List

from extension import app, db

from app.database.models.Teams import Teams


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