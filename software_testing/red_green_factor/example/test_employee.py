"""
Employee class tests.
"""

import unittest

from employee import Employee

NAME: str = "Davi"
EMPLOYEE_ID: int = 123488


class TestEmployeeComputerPayout(unittest.TestCase):
    """Test the compute_payout method of the Employee class."""

    def setUp(self) -> None:
        self.davi = Employee(name=NAME, employee_id=EMPLOYEE_ID)

    def test_employee_payout_returns_float(self):
        """Whether payout returns a float."""
        self.assertIsInstance(self.davi.compute_payout(), float)

    def test_employee_payout_no_commission_no_hours(self):
        """Whether payout is correctly computed in case of no commission and no hours worked."""
        self.assertAlmostEqual(self.davi.compute_payout(), 1000.0)

    def test_employee_payout_no_commission(self):
        """Whether payout is correctly computed in case of no commission and 10 hours worked."""
        self.davi.hours_worked = 10.0
        self.assertAlmostEqual(self.davi.compute_payout(), 2000.0)

    def test_employee_payout_with_commission(self):
        """Whether payout is correctly computed in case of 10 contracts landed and 10 hours worked."""
        self.davi.hours_worked = 10.0
        self.davi.contracts_landed = 10
        self.assertAlmostEqual(self.davi.compute_payout(), 3000.0)

    def test_employee_payout_with_commission_disabled(self):
        """
        Whether payout is correctly computed in case of 10 contracts landed and 10 hours worked
        but commission is disabled.
        """
        self.davi.hours_worked = 10.0
        self.davi.contracts_landed = 10
        self.davi.has_commission = False
        self.assertAlmostEqual(self.davi.compute_payout(), 2000.0)


if __name__ == "__main__":
    unittest.main()
