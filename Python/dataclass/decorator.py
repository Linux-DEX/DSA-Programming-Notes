
# Function Decorator

def decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()

"""
output: 
    Before the function is called.
    Hello!
    After the function is called.
"""


# Decorator with Arguments (Parameterized Decorators)

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(times=3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")

"""
output: 
    Hello, Alice!
    Hello, Alice!
    Hello, Alice!
"""


# Method Decorators (For Methods in Classes)

class MyClass:
    def __init__(self, name):
        self.name = name

    def method_decorator(func):
        def wrapper(self, *args, **kwargs):
            print("Before method call.")
            result = func(self, *args, **kwargs)
            print("After method call.")
            return result
        return wrapper

    @method_decorator
    def greet(self):
        print(f"Hello, {self.name}!")

obj = MyClass("Alice")
obj.greet()

"""
output:
    Before method call.
    Hello, Alice!
    After method call.
"""


# Class Decorators

def add_method(cls):
    def new_method(self):
        print(f"New method in class {self.__class__.__name__}")
    
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    def __init__(self, name):
        self.name = name

obj = MyClass("Alice")
obj.new_method()

"""
output: 
    New method in class MyClass
"""


# Built-in Decorators

class MyClass:
    class_variable = "Class variable"

    @staticmethod
    def static_method():
        print("This is a static method.")
    
    @classmethod
    def class_method(cls):
        print(f"This is a class method. Accessing: {cls.class_variable}")

MyClass.static_method()
MyClass.class_method()

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

circle = Circle(5)
print(circle.radius) 
print(circle.area)   


"""
output:
    This is a static method.
    This is a class method. Accessing: Class variable
    5
    78.5
"""


# Functools Decorators

from functools import wraps

def decorator_with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@decorator_with_wraps
def example_function():
    """This is an example function."""
    print("Hello!")

print(example_function.__name__)  
print(example_function.__doc__)   
example_function()


"""
output:
    example_function
    This is an example function.
    Calling example_function
    Hello!
"""