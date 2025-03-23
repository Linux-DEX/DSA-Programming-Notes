from dataclasses import dataclass, field
from typing import ClassVar

"""
class Person:
    name: str 
    age: int 

    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def __repr__(self):
        return f"Point(name={self.name}, age={self.age})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
"""

@dataclass
class Person:
    name: str 
    age: int

"""
the @dataclass will implement below methods
    __init__
    __repr__
    __eq__
"""

p1 = Person(name="Alice", age=23)
p2 = Person(name="Alice", age=23)

print(p1, p2)

print(p1 == p2)


@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str 
    unit_price: float
    quantity_on_hand: int = 0
    sizes: list[str] = field(default=list)
    class_var: ClassVar[int] = 100

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
    

# def func(lst=[]):
#     lst.append(1)
#     print(lst)

# func()  # [1]
# func()  # [1, 1]


# structure of InventoryItem and different function implemented
# help(InventoryItem)


# Inheritance

class Rectangle:
    def __init__(self, height, width):
        print(f"self object of Rectangle -> {self}")
        self.height = width
        self.width = width

@dataclass
class Square(Rectangle):
    side: float 

    def __post_init__(self):
        super().__init__(self.side, self.side)

sqr = Square(20)
print(f"square class -> {sqr}")


@dataclass
class Circule:
    radius: int 

@dataclass
class ColoredCircule:
    radius: int
    color: str 

colorCircule = ColoredCircule(10, "orange")

print(f"color circule -> {colorCircule}")
