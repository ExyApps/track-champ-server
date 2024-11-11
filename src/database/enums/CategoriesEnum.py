from enum import Enum

class CategoriesEnum(Enum):
    TRACK = {
        'label': 'Testes de Pista',
        'tests': [
            'Células'
        ]
    }
    # BODY = {'label': 'Teste Corporal'}

def match_test(label: str) -> CategoriesEnum:
    """
    Find the TestEnum that corresponds to the value

    Parameters
    ----------
        label: str
            The label of the test

    Returns
    -------
        TestEnum
            The test information

    Throws
    ------
        ValueError
            If no match is found
    """
    for test in CategoriesEnum:
        if test.value['label'].lower() == label.lower():
            return test
    raise ValueError('This should never happen')