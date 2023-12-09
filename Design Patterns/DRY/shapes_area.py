"""The DRY (Don't Repeat Yourself) principle is a fundamental concept in software development that encourages writing code that is efficient and maintainable. By avoiding code duplication, you make your code easier to understand, modify, and debug."""

"""Here are a few examples of how to apply the DRY principle in Python:"""


# 1. Using Functions:
def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width


# Calculate the area of two rectangles
area1 = calculate_area(5, 10)
area2 = calculate_area(3, 7)

print(f"Area of rectangle 1: {area1}")
print(f"Area of rectangle 2: {area2}")

"""This code defines a function calculate_area that takes the length and width of a rectangle as arguments and returns its area. This function is used twice to calculate the areas of two different rectangles, avoiding code duplication."""


# 2. Using Classes:
class Shape:
    """Represents a shape with a name and area."""

    def __init__(self, name):
        self.name = name
        self.area = None

    def calculate_area(self):
        raise NotImplementedError("This method must be implemented by subclasses.")


class Rectangle(Shape):
    """Represents a rectangle with length and width."""

    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def calculate_area(self):
        self.area = self.width * self.length
        return self.area


# Create and calculate area of two rectangles
rectangle1 = Rectangle("Rectangle 1", 5, 10)
rectangle2 = Rectangle("Rectangle 2", 3, 7)

rectangle1.calculate_area()
rectangle2.calculate_area()

print(f"Area of rectangle 1: {rectangle1.area}")
print(f"Area of rectangle 2: {rectangle2.area}")

"""This code defines a base class Shape that has a name and an area. The calculate_area method is abstract and must be implemented by subclasses. The Rectangle class inherits from Shape and implements its own calculate_area method that calculates the area of a rectangle based on its length and width. This approach avoids code duplication and makes the code more modular and reusable."""

# 3. Using Loops:
data = [
    {"name": "John Doe", "age": 30},
    {"name": "Jane Doe", "age": 25},
    {"name": "Bob Markov", "age": 23},
    {"name": "Holly Wood", "age": 18},
]

for person in data:
    print(f"Name: {person['name']}, Age: {person['age']}")

"""This code iterates over a list of dictionaries and prints the name and age of each person. This is a simple example, but it demonstrates how loops can be used to avoid code duplication when you need to perform the same operation on multiple items."""
