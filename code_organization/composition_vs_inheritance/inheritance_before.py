from dataclasses import dataclass


@dataclass
class HourlyEmployee:
    """Employee thats paid on number of worked hours."""

    name: str
    id: int
    commission: float = 100
    constracts_landed: float = 0
    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.pay_rate * self.hours_worked 
            + self.employer_cost
            + self.commission * self.constracts_landed
        )


@dataclass
class SalariedEmployee:
    """Employee thats paid on number a fixed monthly salary."""

    name: str
    id: int
    commission: float = 100
    constracts_landed: float = 0
    monthly_salary: float = 0
    percentage: float = 1

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.monthly_salary * self.percentage 
            + self.commission * self.constracts_landed
        )


@dataclass
class Freelancer:
    """Freelancer thats paid on number a fixed monthly salary."""

    name: str
    id: int
    commission: float = 100
    constracts_landed: float = 0
    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self) -> float:
        """Compute how much the freelancer should be paid."""
        return (
            self.pay_rate * self.hours_worked 
            + self.commission * self.constracts_landed
        )


def main():
    """Main function."""

    henry = HourlyEmployee(name="Henry", id=12345, pay_rate=50, hours_worked=100)
    print(f"{henry.name} worked for {henry.hours_worked} hours and earned ${henry.compute_pay()}.")
    
    sarah = SalariedEmployee(name="Sarah", id=67890, monthly_salary=5000, constracts_landed=10)
    print(f"{sarah.name} landed {sarah.constracts_landed} contracts and earned ${sarah.compute_pay()}.")


if __name__ == '__main__':
    main()