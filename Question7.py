class Engine:
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an Engine instance as an attribute

    def start_engine(self):
        print("Car is starting the engine...")
        self.engine.start()

    def stop_engine(self):
        print("Car is stopping the engine...")
        self.engine.stop()

# Demonstrate usage
my_car = Car()
my_car.start_engine()  # Expected output: "Car is starting the engine...\nEngine started."
my_car.stop_engine()   # Expected output: "Car is stopping the engine...\nEngine stopped."
