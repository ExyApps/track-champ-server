from enum import Enum

class GenderEnum(Enum):
    MALE = 'Masculino'
    FEMALE = 'Feminino'
    OTHER = 'Outro'
    PREFER_NOT_TO_SAY = 'Prefiro não dizer'

def match_gender(value: str) -> GenderEnum:
    for gender in GenderEnum:
        if gender.value.lower() == value.lower():
            return gender
    raise ValueError('This should never happen')