from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class Authorizer(ABC):

    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class SMSAuth(Authorizer):
    authorized = False

    def verify_code(self, code):
        print(f"Verifying code: {code}")
        self.authorized = True

    def is_authorized(self):
        return self.authorized

class NotARobot(Authorizer):
    authorized = False

    def not_a_robot(self):
        print("Are you a robot? Naaaa...")
        self.authorized = True

    def is_authorized(self):
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: Authorizer) -> None:
        self.authorizer = authorizer
        self.security_code = security_code
        super().__init__()

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception('Not authorized')
        print('Processing debit paymente type')
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'

class CreditPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code) -> None:
        self.security_code = security_code
        super().__init__()

    def pay(self, order):
        print('Processing credit paymente type')
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'

class PayPalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authorizer: Authorizer) -> None:
        self.authorizer = authorizer
        self.email_address = email_address
        super().__init__()

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print('Processing paypal paymente type')
        print(f'Verifying security code: {self.email_address}')
        order.status = 'paid'


if __name__ == '__main__':
    order = Order()

    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB Cable", 2, 5)

    print(order.total_price())

    authorizer = SMSAuth()
    # robot = NotARobot()

    processor = PayPalPaymentProcessor("davisp@hotmail.com", authorizer)
    authorizer.verify_code(882697)
    # robot.not_a_robot()
    processor.pay(order)