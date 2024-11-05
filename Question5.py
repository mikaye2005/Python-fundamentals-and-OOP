class Rectangle:
    def __init__(self, length, width=None):
        if width is None:
            self.length = length
            self.width = length  # If only one argument, assume it's a square
        else:
            self.length = length
            self.width = width   # If two arguments, use both as length and width

    def calculate_area(self):
        return self.length * self.width

# Test cases
# Create a square with one argument
square = Rectangle(5)
print(f"Square area: {square.calculate_area()}")  # Expected output: 25

# Create a rectangle with two arguments
rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.calculate_area()}")  # Expected output: 24
