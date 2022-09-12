from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str


def main():
    user = User("Davi", "Segundo")
    print(user)


if __name__ == "__main__":
    main()
