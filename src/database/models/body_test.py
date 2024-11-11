from . import db

from datetime import datetime, timezone

class WeightTest(db.Model):
    __tablename__ = 'test_weight'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('acc_user.id'), nullable=False)
    weight = db.Column(db.Float(2), nullable=False)
    height = db.Column(db.Float(2), nullable=False)
    water = db.Column(db.Float(2), nullable=True)
    body_fat = db.Column(db.Float(2), nullable=True)
    visceral_fat = db.Column(db.Integer, nullable=True)
    bmi = db.Column(db.Float(2), nullable=True)
    muscle = db.Column(db.Float(2), nullable=True)
    protein = db.Column(db.Float(2), nullable=True)
    metabolism = db.Column(db.Integer, nullable=True)
    bone_mass = db.Column(db.Float(2), nullable=True)

    created_in = db.Column(db.DateTime, default = datetime.now(timezone.utc))

    def __repr__(self):
        return f'<WeightTest {self.user_id} {self.weight} {self.created_in}>'
    
    def to_json(self, *excluded_fields):
        """
        Transform the class information to a dictionary, and remove unwanted fields

        Returns:
            (dict): The WeightTest in dictionary format
        """
        hidden_fields = ['id'] + excluded_fields
        info = [getattr(self, x) for x in dir(self) if x not in hidden_fields and not x.startswith('__')]
        return info
    
