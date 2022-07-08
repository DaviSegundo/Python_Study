from dataclasses import dataclass, field

@dataclass
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    force: int = 120

    def __post_init__(self) -> None:
        self.sort_index = self.age

    def __str__(self) -> str:
        return f'{self.name}, {self.job}, {self.age}'

if __name__ == '__main__':
    p1 = Person('Davi', 'SW', 18, 80)
    p2 = Person('Segundo', 'SWD', 20, 100)
    p3 = Person('Pinheiro', 'SE', 22)

    print(p1)
    print(p2)
    print(p3)