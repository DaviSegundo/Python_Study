import timeit
from functools import partial


class Person:
    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email


class PersonSlots:
    __slots__ = "name", "address", "email"

    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email


def get_set_delete(person: Person | PersonSlots):
    person.address = "123 Main St"
    _ = person.address
    del person.address


def main_change_dinamic():
    person = Person("Davi", "123 Main St", "davi@sp.com")
    print(person.__dict__)
    person.hi = "well"  # type: ignore
    print(person.__dict__)


def main():
    person = Person("Davi", "123 Main St", "davi@sp.com")
    person_slots = Person("Davi", "123 Main St", "davi@sp.com")

    no_slots = min(timeit.repeat(partial(get_set_delete, person), number=1000000))
    slots = min(timeit.repeat(partial(get_set_delete, person_slots), number=1000000))

    print(f"No slots: {no_slots}")
    print(f"Slots: {slots}")
    print(f"% performance improvement: {(no_slots - slots) / no_slots:.2%}")


if __name__ == "__main__":
    main()
