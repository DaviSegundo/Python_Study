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


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class PaymentProcessor_SMS(PaymentProcessor):
    
    @abstractmethod
    def auth_sms(self, code):
        pass

class DebitPaymentProcessor(PaymentProcessor_SMS):

    def __init__(self, security_code) -> None:
        self.security_code = security_code
        super().__init__()

    def auth_sms(self, code):
        print(f'Verifying SMS code: {code}')
        self.verified = True

    def pay(self, order):
        if not self.verified:
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

class PayPalPaymentProcessor(PaymentProcessor_SMS):

    def __init__(self, email_address) -> None:
        self.email_address = email_address
        super().__init__()

    def auth_sms(self, code):
        print(f'Verifying SMS code: {code}')
        self.verified = True

    def pay(self, order):
        print('Processing paypal paymente type')
        print(f'Verifying security code: {self.email_address}')
        order.status = 'paid'


if __name__ == '__main__':
    order = Order()

    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB Cable", 2, 5)

    print(order.total_price())

    processor = PayPalPaymentProcessor("davisp@hotmail.com")
    processor.pay(order)