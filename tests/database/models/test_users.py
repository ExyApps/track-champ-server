import datetime

from app.database.models.Users import Users

class TestUsers:
    def test_representation(self, user_model: Users):
        """
        Check if the the representation is correct
        """
        representation = str(user_model)

        assert isinstance(representation, str)
        assert representation.startswith('<User ')

    def test_conversion(self, user_model: Users):
        """
        Check if the conversion is correct
        """
        info = user_model.to_json()

        assert isinstance(info, dict)
        assert len(info) > 0