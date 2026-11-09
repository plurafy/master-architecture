from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get_type(self) -> str:
        pass


class Car(Vehicle):
    def get_type(self) -> str:
        return "Car"


class Bike(Vehicle):
    def get_type(self) -> str:
        return "Bike"


class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass


class CarFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Car()


class BikeFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Bike()


if __name__ == "__main__":
    car_factory = CarFactory()
    bike_factory = BikeFactory()

    my_car = car_factory.create_vehicle()
    my_bike = bike_factory.create_vehicle()

    print(my_car.get_type())  # Car
    print(my_bike.get_type())  # Bike
