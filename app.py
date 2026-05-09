# linting-check:flake8 app.py
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


if __name__ == "__main__":
    result1 = add(4, 5)
    result2 = sub(6, 2)
    print(result1, result2)
