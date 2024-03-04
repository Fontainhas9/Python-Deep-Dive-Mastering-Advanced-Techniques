def simple_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper


@simple_decorator
def say_hello():
    print("Hello")


if __name__ == "__main__":
    say_hello()
