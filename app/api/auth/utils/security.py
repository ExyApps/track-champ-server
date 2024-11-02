from typing import Tuple

import bcrypt

def encrypt_password(password: str, salt: str = None) -> Tuple[str]:
    """
    Generate a salt if needed and encrypt the password using it

    Parameters:
        password (str): The password introduced
        salt (str): The salt previously generated, if any

    Returns:
        (tuple): Password encrypted and the corresponding salt

    """
    if salt is None:
        salt = bcrypt.gensalt(12)
    else:
        salt = bytes(salt, 'utf-8')

    return bytes.decode(bcrypt.hashpw(bytes(password, 'utf-8'), salt)), bytes.decode(salt)