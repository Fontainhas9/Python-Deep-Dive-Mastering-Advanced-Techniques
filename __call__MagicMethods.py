from typing import Any


class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        return f"{self.greeting} {name}!"


if __name__ == "__main__":
    hello = Greeter("Hello")

    print(hello("John"))
