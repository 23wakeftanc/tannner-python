"""
Non specific fixtures for use across all tests.

This fixture is accessible to all tests due to its inclusion in conftest.py.

see: https://docs.pytest.org/en/6.2.x/fixture.html
"""


import pytest


@pytest.fixture()
def my_sample_fixture():
    """Place holder, replace with custom fixtures as needed."""
    ...