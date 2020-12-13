import requests


class MockClass:
    def return_1(self):
        return 1


def check_if_true(a, b):
    if a > b:
        return "a > b"
    return "a < b"


def division_by_zero():
    return 2 / 0


if __name__ == '__main__':
    r = requests.get("https://www.google.com")
    print(r.content)


def sum_(a, b):
    return a + b


def subtract(a, b):
    return a - b


def any_function():
    return "Anything"






