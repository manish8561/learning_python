# decorators


from typing import Any


def decorator_function(original_function):
    print("inside the decorator function befor execution")

    def wrapper_function(*args, **kwargs):
        print("inside the wrapper function befor execution")

        return original_function(*args, **kwargs)

    return wrapper_function

# decorator class
class decorator_class(object):

    def __init__(self, original_function) -> None:
        self.original_function = original_function

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print(f"call method executed this before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print("display function ran")


@decorator_class
def display_info(name, age):
    print(f"display info ran with two arguments ({name}, {age})")


display_info("Manish", 38)
display()
