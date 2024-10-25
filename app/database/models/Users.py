from extension import db
from app.database.models.GenderEnum import GenderEnum

class Users(db.Model):
	__tablename__ = 'acc_users'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(110), nullable=False, unique=True)
	firstName = db.Column(db.String(50), nullable=False)
	lastName = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(50), nullable=False, unique=True)
	password = db.Column(db.String(64), nullable=False)
	salt = db.Column(db.String(30), nullable=False)
	birthday = db.Column(db.Date, nullable=False)
	gender = db.Column(db.Enum(GenderEnum), nullable=False)
	profileImage = db.Column(db.String(50), nullable=True)
	activated = db.Column(db.Boolean, nullable=False, default=False)

	createdIn = db.Column(db.DateTime, nullable=False)
	lastLogIn = db.Column(db.DateTime, nullable=True)

	def __repr__(self):
		return f'<User {self.id} {self.name} {self.username} {self.email}>'

	def to_json(self, excuded_fields = []):
		"""
		Transform the class information to a dictionary, and remove unwanted fields

		Returns:
			(dict): The user in dictionary format
		"""
		info = {
			'id': self.id,
			'username': self.username,
			'firstName': self.firstName,
			'lastName': self.lastName,
			'email': self.email,
			'birthday': self.birthday,
			'gender': self.gender.value,
			'profileImage': self.profileImage,
			'activated': self.activated,
			'createdIn': self.createdIn,
			'lastLogIn': self.lastLogIn
		}

		for field in excuded_fields:
			if field in info:
				del info[field]

		return info
