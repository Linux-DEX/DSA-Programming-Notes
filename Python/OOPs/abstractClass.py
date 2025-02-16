# Abstract Classes

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):  # abstract method, to be implemented by subclasses
        pass

    def move(self):  # concrete method with implementation
        return "moving"

    @property
    @abstractmethod
    def species(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"

    @property
    def species(self):
        return "Canine"


def main():
    dog = Dog()
    print(dog.sound())
    print(dog.move())
    # access it like property
    print(dog.species)


if __name__ == "__main__":
    main()
