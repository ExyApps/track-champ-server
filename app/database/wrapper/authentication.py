from typing import *
from datetime import datetime

from extension import app, db

from app.database.models.Users import Users
from app.database.models.GenderEnum import GenderEnum
from app.database.models.SessionTokens import SessionTokens

def account_exists(email: str) -> bool:
    """
    Check if there is an account with the given email

    Parameters:
        email (str): The user's email

    Returns:
        (bool): True if the email is being used, and False otherwise
    """
    with app.app_context():
        return Users.query.filter_by(email=email).first() is not None


def create_new_user(
    username: str,
    first_name: str,
    last_name: str,
    email: str,
    password: str,
    salt: str,
    birthday: str,
    gender: GenderEnum
):
    """
    Create a new user and insert in the database

    Parameters:
        username (str): The user's username
        first_name (str): The user's first name
        last_name (str): The user's last name
        email (str): The user's email
        password (str): The user's password encrypted
        salt (str): The salt associated to the user's password
        birthday (str): The user's birthday
        gender (GenderEnum): The user's gender
    """
    with app.app_context():
        new_user = Users(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            salt=salt,
            birthday=birthday,
            gender=gender,
            created_in=datetime.now(),
        )
        db.session.add(new_user)
        db.session.commit()


def get_user(_id: int):
    """
    Get a user by its id

    Parameters:
        _id (int): The id of the user

    Returns:
        (Users): The user object
    """
    with app.app_context():
        return Users.query.filter_by(id=_id).first()


def update_user(payload: dict):
    """
    Update the user's information

    Parameters:
        payload (dict): Set of attributes and new values
    """
    with app.app_context():
        user = Users.query.filter_by(id = payload['id']).first()

        for k, v in payload.items():
            if k == 'id':
                continue
            setattr(user, k, v)

        db.session.commit()


def get_salt(email: str) -> str:
    """
    Get the salt associated to the account with the given email

    Parameters:
        email (str): The user's email

    Returns:
        (str): The salt used during registration
    """
    with app.app_context():
        return Users.query.filter_by(email=email).first().salt


def login(email: str, password: str) -> Users:
    """
    Check if there is an account with these details

    Parameters:
        email (str): The user's email
        password (str): The user's password

    Returns:
        (Users): The user object
    """
    with app.app_context():
        return Users.query.filter_by(email=email, password=password).first()


def update_last_login(user: Users) -> None:
    """
    Update the last date the user logged in

    Parameters:
        user (Users): The user object
    """
    with app.app_context():
        db_user = Users.query.filter_by(id=user.id).first()
        db_user.last_login = datetime.now()
        db.session.commit()


def username_exists(username: str) -> bool:
    """
    Check if a username is already being used

    Parameters:
        username (str): The user's email

    Returns:
        (bool): True if the username is being used, False otherwise
    """
    with app.app_context():
        return Users.query.filter_by(username=username).first() is not None


def store_session_token(id: int, token: str) -> None:
    """
    Store the session token for a user

    Parameters
    ----------
        id: int
            The user's id

        token: str
            The session token
    """
    with app.app_context():
        st = SessionTokens(user_id = id, token = token)
        db.session.add(st)
        db.session.commit()


def get_user_by_session_token(token: str) -> Union[int, None]:
    """
    Get the user's id using the session token provided

    Parameters
    ----------
        token: str
            The session token of the user

    Returns
    -------
        Union[int, None]
            The user's id if the token exists, otherwise None
    """
    with app.app_context():
        row = SessionTokens.query.filter_by(token = token).first()
        return row.user_id if row else None