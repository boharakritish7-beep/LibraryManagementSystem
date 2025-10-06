from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")


class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} via PayPal")


class LibrarySystem:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def make_payment(self, amount):
        self.payment_method.pay(amount)
