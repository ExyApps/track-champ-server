from typing import List

from flask import current_app as app

from src.database.models.test_category import TestCategory
from src.database.models.test_test import TestTest

def get_category_by_name(name: str) -> TestCategory:
    """
    Get the test category by name

    Parameters
    ----------
        name: str
            The name of the category

    Returns
    -------
        TestCategory
            The TestCategory object
    """
    return TestCategory.query.filter_by(name=name).first()


def get_categories() -> List[TestCategory]:
    """
    Get a list of all the test categories

    Returns
    -------
        List[TestCategory]
            A list with all the TestCategory
    """
    return TestCategory.query.all()


def save_category(name: str) -> TestCategory:
    """
    Create a new category

    Parameters
    ----------
        name: str
            The name of the category

    Returns
    -------
        TestCategory
            The TestCategory object
    """
    cat = TestCategory(name = name)

    db = app.extensions['sqlalchemy']
    db.session.add(cat)
    db.session.commit()
    db.session.refresh(cat)
    
    return cat


def get_category_tests(category: int) -> List[TestTest]:
    """
    Get the tests of a category

    Parameters
    ----------
        category: int
            The category's id

    Returns
    -------
        List[TestTest]
            A list of all the TestTest
    """
    return TestTest.query.filter_by(category=category).all()


def get_test_by_name(name: str) -> TestTest:
    """
    Get the test by name

    Parameters
    ----------
        name: str
            The name of the test

    Returns
    -------
        TestTest
            The TestTest object
    """
    return TestTest.query.filter_by(name=name).first()

def save_test(name: str, category: int) -> TestTest:
    """
    Create a new test

    Parameters
    ----------
        name: str
            The name of the test

    Returns
    -------
        TestTest
            The TestTest object
    """
    test = TestTest(name = name, category=category)

    db = app.extensions['sqlalchemy']
    db.session.add(test)
    db.session.commit()
    db.session.refresh(test)

    return test