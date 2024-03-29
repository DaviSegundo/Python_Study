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
class LineItem:

    name: str
    price: int
    quantity: int

    @property
    def total_price(self) -> int:
        return self.price * self.quantity


@dataclass
class Order:

    items: List[LineItem] = field(default_factory=list)
    _payment_status: PaymentStatus = PaymentStatus.PENDING

    def add_item(self, item: LineItem) -> None:
        self.items.append(item)

    def is_paid(self) -> bool:
        return self._payment_status == PaymentStatus.PAID

    def is_cancelled(self) -> bool:
        return self._payment_status == PaymentStatus.CANCELLED

    def cancel(self) -> None:
        if self._payment_status == PaymentStatus.PAID:
            raise PaymentStatusError("You cant cancel an already paid order.")
        self._payment_status = PaymentStatus.CANCELLED

    def pay(self) -> None:
        if self._payment_status == PaymentStatus.PAID:
            raise PaymentStatusError("Order is already paid.")
        self._payment_status = PaymentStatus.PAID

    # @property
    # def total_price