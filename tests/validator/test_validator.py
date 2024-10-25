from app.validator.validator import Validator

class TestValidator:
    def test_validate_first_name(self, first_name: str):
        success, message = Validator.first_name(first_name)

        assert success
        assert not message


    def test_validate_empty_first_name(self, empty_field: str):
        success, message = Validator.first_name(empty_field)

        assert not success
        assert message


    def test_validate_last_name(self, last_name: str):
        success, message = Validator.last_name(last_name)

        assert success
        assert not message


    def test_validate_empty_last_name(self, empty_field: str):
        success, message = Validator.last_name(empty_field)

        assert not success
        assert message


    def test_validate_username(self, username: str):
        success, message = Validator.username(username)

        assert success
        assert not message


    def test_validate_empty_username(self, empty_field: str):
        success, message = Validator.username(empty_field)

        assert not success
        assert message
    

    def test_validate_email(self, email: str):
        success, message = Validator.email(email)

        assert success
        assert not message


    def test_validate_empty_email(self, empty_field: str):
        success, message = Validator.email(empty_field)

        assert not success
        assert message


    def test_validate_invalid_email(self, invalid_email: str):
        success, message = Validator.email(invalid_email)

        assert not success
        assert message


    def test_validate_date(self, date: str):
        success, message = Validator.date(date)

        assert success
        assert not message


    def test_validate_empty_date(self, empty_field: str):
        success, message = Validator.date(empty_field)

        assert not success
        assert message

    
    def test_validate_invalid_value_date(self, invalid_value_date: str):
        success, message = Validator.date(invalid_value_date)

        assert not success
        assert message


    def test_validate_invalid_format_date(self, invalid_format_date: str):
        success, message = Validator.date(invalid_format_date)

        assert not success
        assert message


    def test_validate_gender(self, gender: str):
        success, message = Validator.gender(gender)

        assert success
        assert not message


    def test_validate_empty_gender(self, empty_field: str):
        success, message = Validator.gender(empty_field)

        assert not success
        assert message

    
    def test_validate_invalid_gender(self, invalid_gender: str):
        success, message = Validator.gender(invalid_gender)

        assert not success
        assert message


    def test_validate_password(self, password: str):
        success, message = Validator.password(password)

        assert success
        assert not message


    def test_validate_empty_password(self, empty_field: str):
        success, message = Validator.password(empty_field)

        assert not success
        assert message

    
    def test_validate_invalid_small_password(self, invalid_small_password: str):
        success, message = Validator.password(invalid_small_password)

        assert not success
        assert message


    def test_validate_invalid_upper_password(self, invalid_upper_password: str):
        success, message = Validator.password(invalid_upper_password)

        assert not success
        assert message

    
    def test_validate_invalid_lower_password(self, invalid_lower_password: str):
        success, message = Validator.password(invalid_lower_password)

        assert not success
        assert message


    def test_validate_invalid_number_password(self, invalid_number_password: str):
        success, message = Validator.password(invalid_number_password)

        assert not success
        assert message

    
    def test_validate_invalid_special_char_password(self, invalid_special_char_password: str):
        success, message = Validator.password(invalid_special_char_password)

        assert not success
        assert message