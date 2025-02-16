# Inteface

from abc import ABC, abstractmethod


# Defining an interface (abstract class with only abstract methods)
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


# Implementing the interface in a class
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

    def stop_engine(self):
        return "Car engine stopped"


# Implementing the interface in another class
class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started"

    def stop_engine(self):
        return "Bike engine stopped"


# vehicle = Vehicle()  # This will raise an error because it's an abstract class
car = Car()
bike = Bike()

print(car.start_engine())
print(bike.stop_engine())
