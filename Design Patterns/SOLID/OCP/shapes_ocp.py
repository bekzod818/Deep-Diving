from math import pi

"""To understand what the open-closed principle is all about, consider the following Shape class:"""


class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2


shape1 = Shape("rectangle", width=5, height=4)
print(shape1.calculate_area())

shape2 = Shape("circle", radius=5)
print(shape2.calculate_area())

"""Imagine that you need to add a new shape, maybe a square. How would you do that? Well, the option here is to add another elif clause to .__init__() and to .calculate_area() so that you can address the requirements of a square shape."""

"""Having to make these changes to create new shapes means that your class is open to modification. That violates the open-closed principle. How can you fix your class to make it open to extension but closed to modification? Here’s a possible solution:"""

print("*" * 20 + " Open-Closed Principle " + "*" * 20)

from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2


rectangle = Rectangle(width=10, height=12)
print(rectangle.calculate_area())

circle = Circle(radius=3)
print(circle.calculate_area())

square = Square(side=4)
print(square.calculate_area())

"""Note: The example above and some examples in the next sections use Python’s ABCs to provide what’s called interface inheritance. In this type of inheritance, subclasses inherit interfaces rather than functionality. In contrast, when classes inherit functionality, then you’re presented with implementation inheritance."""
