from . import db

class TestTest(db.Model):
    __tablename__ = 'test_test'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('test_category.id'), nullable=False)

    def __repr__(self):
        return f'<TestTest {self.id} - {self.name} - {self.category}>'
    

    def to_json(self, *excluded_fields):
        """
        Transform the class information to a dictionary, and remove unwanted fields

        Returns:
            (dict): The user in dictionary format
        """
        info = {
            'id': self.id,
            'name': self.name,
            'category': self.category,
        }

        for field in excluded_fields:
            if field in info:
                del info[field]

        return info
