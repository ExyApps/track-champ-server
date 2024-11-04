import datetime

from app.database.models.Users import Users

class TestUsers:
    def test_representation(self, user: Users):
        """
        Check if the the representation is correct
        """
        representation = str(user)

        assert isinstance(representation, str)
        assert representation.startswith('<User ')

    def test_conversion(self, user: Users):
        """
        Check if the conversion is correct
        """
        info = user.to_json()

        assert isinstance(info, dict)
        assert len(info) > 0