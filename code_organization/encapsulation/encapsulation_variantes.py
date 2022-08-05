from dataclasses import dataclass, field
from enum import Enum
from typing import List


class PaymentStatus(Enum):
    
    CANCELLED = "cancelled"
    PENDING = "pending"
    PAID = "paid"


class PaymentStatusError(Exception):
    pass


@dataclass
class OrderNoEncapsulationNoInformationHidding:
    """Anyone can get the payment status directly via the instance variable.
    There are no boundaries whatsoever.
    """

    payment_status: PaymentStatus = PaymentStatus.PENDING


@dataclass
class OrderEncapsulationNoInformationHidding:
    """There is an interface now that you should use that provides encapsulation.
    Users of this class still need to know that the status is represented by an enum type.
    """

    _payment_status: PaymentStatus = PaymentStatus.PENDING

    def get_payment_status(self) -> PaymentStatus:
        return self._payment_status

    def set_payment_status(self, status: PaymentStatus) -> None:
        if self._payment_status == PaymentStatus.PAID:
            raise PaymentStatusError(
                "You cant change the status of an already paid order."
            )
        self._payment_status = status


@dataclass
class OrderEncapsulationAndInformationHidding:
    """The status variable is set to 'private'. The only thing you are supposed to use is the
    method, you need to knowledge of how status is represented (that information is 'hidden')
    """

    _payment_status: PaymentStatus = PaymentStatus.PENDING

    def is_paid(self) -> bool:
        return self._payment_status == PaymentStatus.PAID

    def is_cancelled(self) -> bool:
        return self._payment_status == PaymentStatus.CANCELLED

    def cancel(self) -> None:
        if self._payment_status == PaymentStatus.PAID:
            raise PaymentStatusError("You cant cancel an already paid order.")
        self._payment_status = PaymentStatus.CANCELLED