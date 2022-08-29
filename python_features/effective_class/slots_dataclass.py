import timeit
from dataclasses import dataclass
from functools import partial


@dataclass(slots=False)
class Person:
    name: str
    address: str
    email: str


@dataclass(slots=True)
class PersonSlots:
    name: str
    address: str
    email: str


def get_set_delete(person: Person | PersonSlots):
    person.address = "123 Main St"
    _ = person.address
    del person.address


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
