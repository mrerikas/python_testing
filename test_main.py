# Test checking sum of 2 numbers
# pip install pytest
# pip install coverage
# coverage run --source="." --omit="*/venv/*" -m pytest
# coverage html main.py
# coverage report main.py

from main import *
import pytest
import requests


def test_website_response():
    response = requests.get("https://www.google.com")
    assert True

@pytest.fixture()
def add_ten():
    return 10


def test_sum_(add_ten):
    assert sum_(1, add_ten) == 11


def test_subtract():
    assert subtract(10, 5) == 5


def test_selector_subtract():
    assert subtract(5, 3) == 2


def test_any_function():
    assert any_function() == 'Anything'

