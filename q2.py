class Cat:
    """a cat"""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} says meow!")

ella = Cat("Ella")
ella.speak()

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says woof!")

lily = Dog("Lily")
lily.speak()