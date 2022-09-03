from datetime import datetime


class Greeting:
    def __init__(self, greeting_intro) -> None:
        self.greeting_intro = greeting_intro

    def greet(self, name: str) -> str:
        return f"{self.greeting_intro}, {name}."

    def greet_list(self, names: list[str]) -> list[str]:
        greeting_list = []
        for name in names:
            greeting_list.append(self.greet(name))

        return greeting_list


def main() -> None:

    current_time = datetime.now()
    if current_time.hour < 12:
        greeting_intro = "Good morning"
    elif 12 <= current_time.hour < 18:
        greeting_intro = "Good afternoon"
    else:
        greeting_intro = "Good evening"

    name = input("Enter your name: ")

    greeting = Greeting(greeting_intro)
    greet = greeting.greet(name)
    print(greet)


if __name__ == "__main__":
    main()