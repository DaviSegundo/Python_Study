import unittest
from unittest.mock import patch

from dii import AuthorizerSMS, Order, PaymentProcessor

class OrderTestCase(unittest.TestCase):

    def test_init(self):
        order = Order()
        self.assertEqual(order.status, "open")

    def test_set_status(self):
        order = Order()
        order.set_status('paid')
        self.assertEqual(order.status, "paid")


class AuthorizerSMSTestCase(unittest.TestCase):

    def test_init_authorized(self):
        auth = AuthorizerSMS()
        self.assertFalse(auth.is_authorized())

    def test_code_decimal(self):
        auth = AuthorizerSMS()
        auth.generate_sms_code()
        self.assertTrue(auth.code.isdecimal())

    def test_authorized_success(self):
        auth = AuthorizerSMS()
        auth.generate_sms_code()
        with patch('builtins.input', return_value=auth.code):
            auth.authorize()
            self.assertTrue(auth.is_authorized())

    @patch('builtins.input', return_value="1234567")
    def test_authorize_fail(self, mocked_input):
        auth = AuthorizerSMS()
        auth.generate_sms_code()
        auth.authorize()
        self.assertFalse(auth.is_authorized())


class PaymentProcessorTestCase(unittest.TestCase):

    def test_payment_success(self):
        # ???
        self.assertTrue(True)

    def test_payment_fail(self):
        # ???
        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()