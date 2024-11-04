import pytest

@pytest.fixture
def login_payload(email, password):
    return {
        'email': email,
        'password': password
    }

@pytest.fixture
def invalid_login_payload(email, empty_field):
    return {
        'email': email,
        'password': empty_field
    }


@pytest.fixture
def register_payload(date, email, first_name, gender, last_name, password):
    return {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'date': date,
        'gender': gender,
        'password': password
    }