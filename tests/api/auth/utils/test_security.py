from app.api.auth.utils.security import encrypt_password

class TestEncryptPassword:
    # Unittests
    def test_encrypt_password(self, password: str):
        enc_pass, salt = encrypt_password(password)

        assert type(enc_pass) == str
        assert len(enc_pass) == 60
        assert type(salt) == str
        assert len(salt) == 29


    def test_encrypt_password_is_equal(self, password: str):
        enc_pass, salt = encrypt_password(password)
        sec_enc_pass, sec_salt = encrypt_password(password, salt)

        assert enc_pass == sec_enc_pass
        assert salt == sec_salt
