from abc import ABC, abstractmethod

"""
Decorator pattern example for a coffee shop.
Allows adding ingredients like milk and sugar dynamically to a coffee order.
"""


class Coffee(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

    def print_order(self):
        print(f"Order: {self.get_description()} | Cost: ${self.get_cost():.2f}")


class SimpleCoffee(Coffee):
    def get_cost(self) -> float:
        return 2.00

    def get_description(self) -> str:
        return "Simple Coffee"


class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def get_cost(self) -> float:
        return self._coffee.get_cost()

    def get_description(self) -> str:
        return self._coffee.get_description()


class MilkDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.50

    def get_description(self) -> str:
        return self._coffee.get_description() + ", Milk"


class SugarDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.30

    def get_description(self) -> str:
        return self._coffee.get_description() + ", Sugar"


if __name__ == "__main__":
    simple_coffee = SimpleCoffee()
    simple_coffee.print_order()

    milk_coffee = MilkDecorator(simple_coffee)
    milk_coffee.print_order()

    sugar_milk_coffee = SugarDecorator(milk_coffee)
    sugar_milk_coffee.print_order()

    sugar_coffee = SugarDecorator(simple_coffee)
    sugar_coffee.print_order()
