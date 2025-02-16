# polymorphism


class Animal:
    def sound(self):
        return "Some generic sound"


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())


# method Overriding


def product(a, b):
    p = a * b
    print(p)


def product(a, b, c):
    p = a * b * c
    print(p)


product(4, 5, 5)
