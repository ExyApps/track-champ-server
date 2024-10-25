import pytest

@pytest.fixture
def empty_field():
    "A test fixture containg an empty value"
    return ""

@pytest.fixture
def first_name():
    "A test fixture containg a valid first name"
    return "John"

@pytest.fixture
def last_name():
    "A test fixture containg a valid last name"
    return "Doe"

@pytest.fixture
def username():
    "A test fixture containg a valid username"
    return "johndoe"

@pytest.fixture
def email():
    "A test fixture containg a valid email"
    return "johndoe@gmail.com"

@pytest.fixture
def invalid_email():
    "A test fixture containg an invalid email"
    return "johndoe@gmail"

@pytest.fixture
def date():
    "A test fixture containg a valid date"
    return "2000-01-01"

@pytest.fixture
def invalid_value_date():
    "A test fixture containg an invalid date"
    return "2000-13-01"

@pytest.fixture
def invalid_format_date():
    "A test fixture containg an invalid date"
    return "2000/01/01"

@pytest.fixture
def gender():
    "A test fixture containg a valid gender"
    return 'Masculino'

@pytest.fixture
def invalid_gender():
    "A test fixture containg an invalid gender"
    return 'NotGender'

@pytest.fixture
def password():
    "A test fixture containg a valid password"
    return 'Password1!'

@pytest.fixture
def invalid_small_password():
    "A test fixture containg an invalid password"
    return '1234'

@pytest.fixture
def invalid_upper_password():
    "A test fixture containg an invalid password"
    return 'password1!'

@pytest.fixture
def invalid_lower_password():
    "A test fixture containg an invalid password"
    return 'PASSWORD1!'

@pytest.fixture
def invalid_number_password():
    "A test fixture containg an invalid password"
    return 'Password!'

@pytest.fixture
def invalid_special_char_password():
    "A test fixture containg an invalid password"
    return 'Password1'
