from typing import *
from datetime import datetime

from flask import current_app as app

from src.database.models.user import User
from src.database.enums.GenderEnum import GenderEnum
from src.database.models.session_token import SessionToken

def get_account_by_email(email: str) -> Optional[User]:
    """
    Get an account by its email if it exists

    Parameters
    ----------
        email: str
            The user's email

    Returns
    -------
        Optional[User]: The user information
    """
    return User.query.filter_by(email=email).first()


def account_exists(email: str) -> bool:
    """
    Check if there is an account with the given email

    Parameters:
        email (str): The user's email

    Returns:
        (bool): True if the email is being used, and False otherwise
    """
    return User.query.filter_by(email=email).first() is not None


def create_new_user(
    username: str,
    first_name: str,
    last_name: str,
    email: str,
    password: str,
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
        birthday (str): The user's birthday
        gender (GenderEnum): The user's gender
    """
    new_user = User(
		username=username,
		first_name=first_name,
		last_name=last_name,
		email=email,
		password=password,
		birthday=birthday,
		gender=gender,
		created_in=datetime.now(),
	)

    db = app.extensions['sqlalchemy']
    db.session.add(new_user)
    db.session.commit()


def get_user(_id: int):
    """
    Get a user by its id

    Parameters:
        _id (int): The id of the user

    Returns:
        (User): The user object
    """
    return User.query.filter_by(id=_id).first()


def update_user(id: int, payload: dict):
    """
    Update the user's information

    Parameters:
        id (int): The user's id
        payload (dict): Set of attributes and new values
    """
    user = User.query.filter_by(id = id).first()

    for k, v in payload.items():
        setattr(user, k, v)

    user.birthday = datetime.strptime(payload['date'], '%Y-%m-%d')

    db = app.extensions['sqlalchemy']
    db.session.commit()


def get_salt(email: str) -> str:
    """
    Get the salt associated to the account with the given email

    Parameters:
        email (str): The user's email

    Returns:
        (str): The salt used during registration
    """
    return User.query.filter_by(email=email).first().salt


def login(email: str, password: str) -> User:
    """
    Check if there is an account with these details

    Parameters:
        email (str): The user's email
        password (str): The user's password

    Returns:
        (User): The user object
    """
    return User.query.filter_by(email=email, password=password).first()


def update_last_login(user: User) -> None:
    """
    Update the last date the user logged in

    Parameters:
        user (User): The user object
    """
    db_user = User.query.filter_by(id=user.id).first()
    db_user.last_login = datetime.now()

    db = app.extensions['sqlalchemy']
    db.session.commit()


def username_exists(username: str) -> bool:
    """
    Check if a username is already being used

    Parameters:
        username (str): The user's email

    Returns:
        (bool): True if the username is being used, False otherwise
    """
    return User.query.filter_by(username=username).first() is not None


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
    st = SessionToken(user_id = id, token = token)

    db = app.extensions['sqlalchemy']
    db.session.add(st)
    db.session.commit()


def delete_session_token(id: int, token: str) -> None:
    """
    Delete a session token

    Parameters
    ----------
        id: int
            The user's id

        token: str
            The session token
    """
    st = SessionToken.query.filter_by(user_id=id, token=token).first()

    db = app.extensions['sqlalchemy']
    db.session.delete(st)
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
    row = SessionToken.query.filter_by(token = token).first()
    return row.user_id if row else None