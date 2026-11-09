from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, card_holder: str, cvv: str, expiry_date: str):
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv
        self.expiry_date = expiry_date

    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Credit Card ending with {self.card_number[-4:]}")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using PayPal account {self.email}")


class OrderContext:
    def __init__(self):
        self.payment_strategy = None

    def set_payment_strategy(self, payment_strategy: PaymentStrategy) -> None:
        self.payment_strategy = payment_strategy

    def checkout(self, amount: float) -> None:
        if not self.payment_strategy:
            print("Please select a payment method before checking out.")
            return
        self.payment_strategy.pay(amount)


if __name__ == "__main__":
    order = OrderContext()
    order.set_payment_strategy(
        CreditCardPayment("1234567890123456", "John Doe", "123", "12/25")
    )
    order.checkout(100.0)

    order.set_payment_strategy(PayPalPayment("john.doe@example.com"))
    order.checkout(200.0)
