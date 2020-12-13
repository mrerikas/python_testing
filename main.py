import requests

if __name__ == '__main__':
    r = requests.get("https://www.google.com")
    print(r.content)


def sum_(a, b):
    return a + b


def subtract(a, b):
    return a - b


def any_function():
    return "Anything"






