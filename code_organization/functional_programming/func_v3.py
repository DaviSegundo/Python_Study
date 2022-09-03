from datetime import datetime
from typing import Callable
from functools import partial


GreetingReader = Callable[[], str]


def greet(name: str, greeting_reader: GreetingReader) -> str:
    if name == "Davi":
        return "Kekw!"
    return f"{greeting_reader()}, {name}."


def greet_list(names: list[str], greeting_reader: GreetingReader) -> list[str]:
    return [greet(name, greeting_reader) for name in names]


def read_greeting() -> str:
    current_time = datetime.now()
    if current_time.hour < 12:
        return "Good morning"
    if 12 <= current_time.hour < 18:
        return "Good afternoon"
    return "Good evening"


def read_name() -> str:
    return input("Enter your name: ")


def main() -> None:
    greet_fn = partial(greet, greeting_reader=read_greeting)
    print(greet_fn(read_name()))
    print(greet_list(["Davi", "Segundo", "Pinheiro"], read_greeting))


if __name__ == "__main__":
    main()
