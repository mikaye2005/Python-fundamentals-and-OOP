class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Test the functionality
vector1 = Vector(3, 4)
vector2 = Vector(1, 2)

# Adding two vectors
result = vector1 + vector2
print(result)  # Expected output: Vector(4, 6)
