from datetime import datetime

from extension import app, db

from app.database.models.Users import Users
from app.database.models.GenderEnum import GenderEnum

def account_exists(email: str) -> bool:
	with app.app_context():
		return Users.query.filter_by(email=email).first() is not None
		

def create_new_user(
	username: str,
	first_name: str,
	last_name: str,
	email: str,
	password: str,
	salt: str,
	birthday: datetime,
	gender: GenderEnum
):
	with app.app_context():
		new_user = Users(
			username=username,
			firstName=first_name,
			lastName=last_name,
			email=email,
			password=password,
			salt=salt,
			birthday=birthday,
			gender=gender,
			createdIn=datetime.now(),
		)
		db.session.add(new_user)
		db.session.commit()


def get_user(_id: int):
	with app.app_context():
		return Users.query.filter_by(id=_id).first()


def update_user(payload: dict):
	with app.app_context():
		user = Users.query.filter_by(id = payload['id']).first()

		for k, v in payload.items():
			if k == 'id': continue
			setattr(user, k, v)

		db.session.commit()


def get_salt(email: str) -> str:
	with app.app_context():
		return Users.query.filter_by(email=email).first().salt


def login(email: str, password: str) -> Users:
	with app.app_context():
		return Users.query.filter_by(email=email, password=password).first()
	
def update_last_login(user: Users) -> None:
	with app.app_context():
		db_user = Users.query.filter_by(id=user.id).first()
		db_user.lastLogIn = datetime.now()
		db.session.commit()


def username_exists(username: str) -> bool:
	with app.app_context():
		return Users.query.filter_by(username=username).first() is not None