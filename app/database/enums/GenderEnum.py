from enum import Enum

class GenderEnum(Enum):
    MALE = 'Masculino'
    FEMALE = 'Feminino'
    OTHER = 'Outro'
    PREFER_NOT_TO_SAY = 'Prefiro não dizer'

def match_gender(value: str) -> GenderEnum:
    """
    Find the GenderEnum that corresponds to the value

    Parameters:
        value (str): The enum value to be matched

    Returns:
        (GenderEnum): The GenderEnum that corresponds to the given value

    Throws:
        (ValueError): If no match is found
    """
    for gender in GenderEnum:
        if gender.value.lower() == value.lower():
            return gender
    raise ValueError('This should never happen')
