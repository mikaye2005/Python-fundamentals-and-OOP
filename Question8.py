class Calculator:
    count = 0  # Static attribute to track method calls

    @staticmethod
    def add(a, b):
        Calculator.count += 1  # Increment count each time add() is called
        return a + b

# Demonstrate usage
# Using the static method add() and updating the count
result1 = Calculator.add(5, 3)
print(f"Result of addition: {result1}")  # Expected output: 8
print(f"Add method called: {Calculator.count} time(s)")

result2 = Calculator.add(10, 20)
print(f"Result of addition: {result2}")  # Expected output: 30
print(f"Add method called: {Calculator.count} time(s)")
