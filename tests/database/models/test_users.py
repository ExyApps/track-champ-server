import datetime

from app.database.models.user import User

class TestUser:
    def test_representation(self, user: User):
        """
        Check if the the representation is correct
        """
        representation = str(user)

        assert isinstance(representation, str)
        assert representation.startswith('<User ')

    def test_conversion(self, user: User):
        """
        Check if the conversion is correct
        """
        info = user.to_json()

        assert isinstance(info, dict)
        assert len(info) > 0