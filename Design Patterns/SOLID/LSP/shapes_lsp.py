class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


"""Because a square is a special case of a rectangle with equal sides, you think of deriving a Square class from Rectangle in order to reuse the code. Then, you override the setter method for the .width and .height attributes so that when one side changes, the other side also changes:"""


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        if name in ["width", "height"]:
            self.__dict__["width"] = value
            self.__dict__["height"] = value


"""In this snippet of code, you’ve defined Square as a subclass of Rectangle. As a user might expect, the class constructor takes only the side of the square as an argument. Internally, the .__init__() method initializes the parent’s attributes, .width and .height, with the side argument."""

square = Square(side=5)
print(vars(square))
print(square.calculate_area())

square.width = 7
print(vars(square))
print(square.calculate_area())

square.height = 9
print(vars(square))
print(square.calculate_area())

"""Now you’ve ensured that the Square object always remains a valid square, making your life easier for the small price of a bit of wasted memory. Unfortunately, this violates the Liskov substitution principle because you can’t replace instances of Rectangle with their Square counterparts."""

"""When someone expects a rectangle object in their code, they might assume that it’ll behave like one by exposing two independent .width and .height attributes. Meanwhile, your Square class breaks that assumption by changing the behavior promised by the object’s interface. That could have surprising and unwanted consequences, which would likely be hard to debug."""

"""While a square is a specific type of rectangle in mathematics, the classes that represent those shapes shouldn’t be in a parent-child relationship if you want them to comply with the Liskov substitution principle. One way to solve this problem is to create a base class for both Rectangle and Square to extend:"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2


"""Shape becomes the type that you can substitute through polymorphism with either Rectangle or Square, which are now siblings rather than a parent and a child. Notice that both concrete shape types have distinct sets of attributes, different initializer methods, and could potentially implement even more separate behaviors. The only thing that they have in common is the ability to calculate their area."""

print("*" * 20 + " Liskov Substitution Principle " + "*" * 20)

square = Square(side=4)
print(vars(square))
print(square.calculate_area())

rectangle = Rectangle(width=3, height=4)
print(vars(rectangle))
print(rectangle.calculate_area())


def get_total_area(shapes: list):
    return sum([shape.calculate_area() for shape in shapes])


shapes = [Rectangle(width=2, height=4), Square(side=5)]
print(get_total_area(shapes))
