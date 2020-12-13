# Test checking sum of 2 numbers
# pip install pytest
# pip install coverage
# coverage run --source="." --omit="*/venv/*" -m pytest
# coverage html main.py
# coverage report main.py

from main import *
import pytest
import requests
import mock
from main import MockClass


def test_check_if_true():
    with pytest.raises(ZeroDivisionError):
        assert division_by_zero()
    assert check_if_true(1, 2) == 'a < b'
    assert check_if_true(2, 1) == 'a > b'


def test_mock_class_return_one():
    with mock.patch.object(MockClass, 'return_1', 3):
        instance_of_mock_class = MockClass()
        x = instance_of_mock_class.return_1
        assert x == 3


def test_class_return_one():
    instance_of_mock_class = MockClass()
    x = instance_of_mock_class.return_1()
    assert x == 1


@mock.patch('requests.get')
def test_website_response(mock_get):
    mock_get.return_value.status_code = 200
    response = requests.get("https://www.google.com/")
    assert response.status_code == 200


@pytest.fixture()
def add_ten():
    return 10


test_data = [
    (1, 1, 2),
    (2, 2, 4),
    (2, 3, 5),
    (5, 4, 9)
]


@pytest.mark.parametrize("a, b, expected", test_data)
def test_sum_(a, b, expected):
    assert sum_(a, b) == expected


def test_subtract():
    assert subtract(10, 5) == 5


def test_selector_subtract():
    assert subtract(5, 3) == 2


def test_any_function():
    assert any_function() == 'Anything'

