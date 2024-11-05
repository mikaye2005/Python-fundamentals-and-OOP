from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Create instances of Circle and Square
circle = Circle(5)
square = Square(4)

# Call area() on each
print(f"Circle area: {circle.area():.2f}")  # Expected output: Circle area: 78.54
print(f"Square area: {square.area()}")      # Expected output: Square area: 16
