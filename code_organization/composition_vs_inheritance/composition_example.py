from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional


@dataclass
class Comission(ABC):
    """Represents a generic commission."""

    commission: float = 100
    constracts_landed: float = 0

    @abstractmethod
    def get_payment(self) -> float:
        """Compute the commision to be paid out."""


@dataclass
class ContractComission(Comission):
    """Represents a commission."""

    commission: float = 100
    constracts_landed: float = 0

    def get_payment(self) -> float:
        return (self.commission * self.constracts_landed)


class Contract(ABC):
    """Represents a contract and payment process for a particular employee."""

    @abstractmethod
    def get_payment(self) -> float:
        """Compute how much to pay an employee under this contract"""


@dataclass
class HourlyContract(Contract):
    """Contract type for an employee thays paid on number of worked hours."""

    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        return (self.pay_rate * self.hours_worked + self.employer_cost)


@dataclass
class SalariedContract(Contract):
    """Contract type for a employee thats paid on number a fixed monthly salary."""

    monthly_salary: float = 0
    percentage: float = 1

    def get_payment(self) -> float:
        return (self.monthly_salary * self.percentage)


@dataclass
class FreelancerContract(Contract):
    """Freelancer thats paid on number a fixed monthly salary."""

    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self) -> float:
        return (self.pay_rate * self.hours_worked)


@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    name: str
    id: int
    contract: Contract
    commission: Optional[Comission] = None

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()
        return payout


def main():
    """Main function."""

    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=12345, contract=henry_contract)
    print(f"{henry.name} worked for {henry_contract.hours_worked} hours and earned ${henry.compute_pay()}.")
    
    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = ContractComission(constracts_landed=10)
    sarah = Employee(name="Sarah", id=67890, contract=sarah_contract, commission=sarah_commission)
    print(f"{sarah.name} landed {sarah_commission.constracts_landed} contracts and earned ${sarah.compute_pay()}.")


if __name__ == '__main__':
    main()