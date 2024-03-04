from distutils import debug


def repeat(num):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat


@repeat(num=3)
def great(name):
    print("Hello", name)


def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function {func.__name__}({args}, {kwargs}) returned {result}")
        return result
    return wrapper


@debug
def add(a, b):
    return a + b


if __name__ == "__main__":
    # great("Armando")
    print(add(2, b=3))
