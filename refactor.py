from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class CLT(Enum):
    JUNIOR = 5000
    PLENO = 8000
    SENIOR = 12000

class PJ(Enum):
    JUNIOR = 30
    PLENO = 50
    SENIOR = 80

@dataclass
class Empregado(ABC):
    name: str
    age: int
    hours: int

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @abstractmethod
    def pay(self):
        pass

@dataclass
class EmpregadoPJ(Empregado):
    level: PJ

    def pay(self):
        total = self.hours * self.level.value
        print(total)

@dataclass
class EmpregadoCLT(Empregado):
    level: CLT

    def pay(self):
        total = self.level.value
        print(total)


if __name__ == '__main__':
    em1 = EmpregadoCLT('Davi', 18, 40, CLT.PLENO)
    em2 = EmpregadoPJ('Segundo', 22, 120, PJ.PLENO)

    em1.show_info()
    em2.show_info()

    em1.pay()
    em2.pay()
