from enum import Enum

class TestEnum(Enum):
    BODY = {'label': 'Teste Corporal', 'model': 'BodyTest'}

def match_test(label: str) -> TestEnum:
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
    for test in TestEnum:
        if test.value['label'].lower() == label.lower():
            return test
    raise ValueError('This should never happen')