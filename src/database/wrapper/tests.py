from typing import List
from datetime import datetime

from flask import current_app as app

from src.database.models.test_category import TestCategory
from src.database.models.test_test import TestTest
from src.database.models.test_event import TestEvent
from src.database.models.tests.race_test import RaceTest

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


def get_category_by_id(id: int) -> TestCategory:
    """
    Get the test category by id

    Parameters
    ----------
        id: int
            The id of the category

    Returns
    -------
        TestCategory
            The TestCategory object
    """
    return TestCategory.query.get(id)


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


def get_test_by_id(id: int) -> TestTest:
    """
    Get the test by id

    Parameters
    ----------
        id: int
            The id of the test

    Returns
    -------
        TestTest
            The TestTest object
    """
    return TestTest.query.get(id)


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


##################
# Test Creation
##################
def create_test_event(category: int, test: int, athlete: int, date: datetime = None) -> TestEvent:
    """
    Create a test event

    Parameters
    ----------
        category: int
            The category's id

        test: int
            The test's id

        athlete: int
            The athlete's id

        date: datetime
            The date of the test

    Returns
    -------
        RaceTest
            The object created
    """
    test_event = TestEvent(
        category_id=category,
        test_id=test,
        user_id=athlete,
        date=date
    )

    db = app.extensions['sqlalchemy']
    db.session.add(test_event)
    db.session.commit()
    db.session.refresh(test_event)

    return test_event


def create_race_result(test_event_id: int, payload: dict) -> RaceTest:
    """
    Upload a race result

    Parameters
    ----------
        payload: dict
            The information regarding the result

    Returns
    -------
        RaceTest
            The object created
    """
    result = RaceTest(
        distance = payload['distance'],
        time = payload['time'],
        test_event_id=test_event_id
    )

    db = app.extensions['sqlalchemy']
    db.session.add(result)
    db.session.commit()
    db.session.refresh(result)

    return result