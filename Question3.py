class Animal:
    def eat(self):
        print("The animal is eating.")

    def sleep(self):
        print("The animal is sleeping.")

class Dog(Animal):
    def bark(self):
        print("The dog is barking.")

# Create an instance of Dog
my_dog = Dog()

# Using inherited methods from Animal
my_dog.eat()    # Should print: "The animal is eating."
my_dog.sleep()  # Should print: "The animal is sleeping."

# Using the new method in Dog
my_dog.bark()   # Should print: "The dog is barking."
