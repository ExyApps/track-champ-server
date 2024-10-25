from app.api.auth.utils.codes import generate_digit_code
from app.api.auth.utils.codes import generate_session_cookie

class TestGenerateDigitCode:
    # Common Verifications
    def type_is_correct(self, code: str):
        """
        Check if the argument is a string
        """
        return type(code) == str
    
    def format_is_valid(self, code: str):
        """
        Check if the argument is a digit
        """
        return code.isdigit()

    # Unittests
    def test_generate_digit_code_len_6(self):
        """
        Check if the code generated has the desired size and type
        """
        code = generate_digit_code(6)

        assert self.type_is_correct(code)
        assert self.format_is_valid(code)
        assert len(code) == 6

    def test_generate_digit_code_len_10(self):
        """
        Check if the code generated has the desired size and type
        """
        code = generate_digit_code(10)

        assert self.type_is_correct(code)
        assert self.format_is_valid(code)
        assert len(code) == 10


class TestGenerateSessionCookie:
    # Common Verifications
    def type_is_correct(self, cookie: str):
        """
        Check if the argument is a string
        """
        return type(cookie) == str
    
    def format_is_valid(self, cookie: str):
        """
        Check if the argument is a alpha numeric and lower case
        """
        return cookie.isalnum() and cookie.lower() == cookie
    
    # Unittests
    def test_generate_session_cookie(self):
        """
        Check if the code generated has the desired size and type
        """
        cookie = generate_session_cookie()

        assert self.type_is_correct(cookie)
        assert self.format_is_valid(cookie)
        assert len(cookie) == 32