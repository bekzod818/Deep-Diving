def say_goodbye(func):
    def wrapper(name):
        result = func(name)
        action, name = result.split()
        return f"Goodbye, {name}"

    return wrapper


@say_goodbye
def function(name: str) -> str:
    return f"Hello, {name}!"


print(function("Bekzod"))
