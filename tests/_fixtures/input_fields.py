import pytest

@pytest.fixture
def empty_field(): return ""

@pytest.fixture
def first_name(): return "John"

@pytest.fixture
def last_name(): return "Doe"

@pytest.fixture
def username(): return "johndoe"

@pytest.fixture
def email(): return "johndoe@gmail.com"

@pytest.fixture
def invalid_email(): return "johndoe@gmail"

@pytest.fixture
def date(): return "2000-01-01"

@pytest.fixture
def invalid_value_date(): return "2000-13-01"

@pytest.fixture
def invalid_format_date(): return "2000/01/01"

@pytest.fixture
def gender(): return 'Masculino'

@pytest.fixture
def invalid_gender(): return 'NotGender'

@pytest.fixture
def password(): return 'Password1!'

@pytest.fixture
def invalid_small_password(): return '1234'

@pytest.fixture
def invalid_upper_password(): return 'password1!'

@pytest.fixture
def invalid_lower_password(): return 'PASSWORD1!'

@pytest.fixture
def invalid_number_password(): return 'Password!'

@pytest.fixture
def invalid_special_char_password(): return 'Password1'