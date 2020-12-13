import requests

if __name__ == '__main__':
    response = requests.get("https://www.google.com")
    print(response.content)


def sum_(a, b):
    return a + b


def subtract(a, b):
    return a - b


def any_function():
    return "Anything"






