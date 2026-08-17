from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


class DebitCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Debit Card.")


class UpiPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


class CashPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash.")


# Context Class
class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Main Program
if __name__ == "__main__":

    amount = float(input("Enter payment amount: "))

    print("\nChoose Payment Method:")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. UPI")
    print("4. Cash")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        strategy = CreditCardPayment()
    elif choice == 2:
        strategy = DebitCardPayment()
    elif choice == 3:
        strategy = UpiPayment()
    elif choice == 4:
        strategy = CashPayment()
    else:
        print("Invalid choice!")
        exit()

    processor = PaymentProcessor(strategy)
    processor.process_payment(amount)