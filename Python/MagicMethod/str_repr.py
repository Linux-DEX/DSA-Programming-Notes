class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

    def __repr__(self):
        return f"Car('{self.make}', '{self.model}', {self.year})"


car = Car("Toyota", "Camry", 2022)
print(str(car)) # Output: Toyota Camry 2022
print(repr(car)) # Output: Car('Toyota', 'Camry', 2022)
