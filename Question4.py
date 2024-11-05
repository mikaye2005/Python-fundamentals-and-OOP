class Cat:
    def make_sound(self):
        print("Meow!")

class Dog:
    def make_sound(self):
        print("Woof!")

def animal_sound(animal):
    animal.make_sound()

# Create instances of Cat and Dog
my_cat = Cat()
my_dog = Dog()

# Demonstrate polymorphism
animal_sound(my_cat)  # Expected output: "Meow!"
animal_sound(my_dog)  # Expected output: "Woof!"
