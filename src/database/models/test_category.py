from . import db

class TestCategory(db.Model):
    __tablename__ = 'test_category'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return f'<TestCategory {self.id} - {self.name}>'
    

    def to_json(self, *excluded_fields):
        """
        Transform the class information to a dictionary, and remove unwanted fields

        Returns:
            (dict): The user in dictionary format
        """
        info = {
            'id': self.id,
            'name': self.name,
        }

        for field in excluded_fields:
            if field in info:
                del info[field]

        return info
