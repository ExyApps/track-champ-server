import pytest

from app.database.models.GenderEnum import GenderEnum
from app.database.models.GenderEnum import match_gender

class TestGenderEmail:
    def test_get_male_gender(self):
        """
        Check if the right GenderEnum is obtained
        """
        value_gender = 'Masculino'
        gender = match_gender(value_gender)

        assert isinstance(gender, GenderEnum)
        assert gender.value == value_gender

    
    def test_get_female_gender(self):
        """
        Check if the right GenderEnum is obtained
        """
        value_gender = 'Feminino'
        gender = match_gender(value_gender)

        assert isinstance(gender, GenderEnum)
        assert gender.value == value_gender

    
    def test_get_other_gender(self):
        """
        Check if the right GenderEnum is obtained
        """
        value_gender = 'Outro'
        gender = match_gender(value_gender)

        assert isinstance(gender, GenderEnum)
        assert gender.value == value_gender


    def test_get_prefer_not_to_say_gender(self):
        """
        Check if the right GenderEnum is obtained
        """
        value_gender = 'Prefiro não dizer'
        gender = match_gender(value_gender)

        assert isinstance(gender, GenderEnum)
        assert gender.value == value_gender


    def test_gender_not_found(self):
        """
        Check if an error is thrown
        """
        value_gender = 'None'

        with pytest.raises(ValueError):
            gender = match_gender(value_gender)