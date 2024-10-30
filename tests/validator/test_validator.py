from app.validator.validator import Validator

class TestValidator:
    def test_validate_normal_string(self, first_name: str):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload(
            {'normal_string': first_name}
        )

        assert not errors


    def test_validate_empty_string(self, empty_field: str):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload({
            'empty_string': empty_field
        })

        assert len(errors) == 1


    def test_validate_boolean_field(self, boolean_field: bool):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload(
            {'bool': boolean_field}
        )

        assert not errors

    
    def test_validate_ignore_field(self, first_name):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload(
            {'id': first_name}
        )

        assert not errors


    def test_validate_email(self, email: str):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload({
            'email': email
        })

        assert not errors


    def test_validate_invalid_email(self, invalid_email: str):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload({
            'email': invalid_email
        })

        assert len(errors) == 1


    def test_validate_date(self, date: str):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload({
            'date': date
        })

        assert not errors


    def test_validate_invalid_value_date(self, invalid_value_date: str):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload({
            'date': invalid_value_date
        })

        assert len(errors) == 1


    def test_validate_invalid_format_date(self, invalid_format_date: str):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload({
            'date': invalid_format_date
        })

        assert len(errors) == 1


    def test_validate_gender(self, gender: str):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload({
            'gender': gender
        })

        assert not errors


    def test_validate_invalid_gender(self, invalid_gender: str):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload({
            'gender': invalid_gender
        })

        assert len(errors) == 1


    def test_validate_password(self, password: str):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload({
            'password': password
        })

        assert not errors


    def test_validate_invalid_small_password(self, invalid_small_password: str):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload({
            'password': invalid_small_password
        })

        assert len(errors) == 1


    def test_validate_invalid_upper_password(self, invalid_upper_password: str):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload({
            'password': invalid_upper_password
        })

        assert len(errors) == 1


    def test_validate_invalid_lower_password(self, invalid_lower_password: str):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload({
            'password': invalid_lower_password
        })

        assert len(errors) == 1


    def test_validate_invalid_number_password(self, invalid_number_password: str):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload({
            'password': invalid_number_password
        })

        assert len(errors) == 1


    def test_validate_invalid_special_char_password(self, invalid_special_char_password: str):
        """
        Check if the field is valid
        """
        errors = Validator.validate_payload({
            'password': invalid_special_char_password
        })

        assert len(errors) == 1
