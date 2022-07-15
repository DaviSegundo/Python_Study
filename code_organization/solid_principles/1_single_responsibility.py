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


class Paymentprocessor:
    def pay_credit(self, order, security_code):
        print('Processing credit paymente type')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'

    def pay_debit(self, order, security_code):
        print('Processing debit paymente type')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'

if __name__ == '__main__':
    order = Order()

    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB Cable", 2, 5)

    print(order.total_price())

    processor = Paymentprocessor()
    processor.pay_debit(order, "0372846")