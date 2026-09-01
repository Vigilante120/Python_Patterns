# Basic class definition
class Dog:
    # Class variable (shared across all instances)
    species = "Canis familiaris"
    
    # Constructor - initializes instance variables
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    # Instance method
    def bark(self):
        return f"{self.name} says: Woof!"
    
    # Instance method with calculation
    def human_age(self):
        return self.age * 7
    
    # String representation
    def __str__(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}"
    
    # Representation for debugging
    def __repr__(self):
        return f"Dog('{self.name}', {self.age}, '{self.breed}')"


# Creating instances
dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 5, "Labrador")

# Using instance methods
print(dog1.bark())                  # Buddy says: Woof!
print(dog2.human_age())             # 35

# Using __str__
print(dog1)                         # Buddy is a 3-year-old Golden Retriever

# Accessing class variable
print(dog1.species)                 # Canis familiaris


# ===== INHERITANCE EXAMPLE =====
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return "Some generic sound"


class Cat(Animal):  # Inherits from Animal
    def make_sound(self):  # Override method
        return f"{self.name} says: Meow!"


cat = Cat("Whiskers")
print(cat.make_sound())             # Whiskers says: Meow!


# ===== ENCAPSULATION EXAMPLE =====
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable (name mangling with __)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}"
        return "Invalid or insufficient funds"
    
    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
print(account.deposit(500))          # Deposited $500
print(account.get_balance())         # 1500
print(account.withdraw(200))         # Withdrew $200


# ===== CLASS METHOD & STATIC METHOD =====
class Circle:
    pi = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.pi * self.radius ** 2
    
    @classmethod
    def from_diameter(cls, diameter):
        """Create a circle from diameter"""
        return cls(diameter / 2)
    
    @staticmethod
    def is_valid_radius(radius):
        """Check if radius is valid (doesn't need self or cls)"""
        return radius > 0


circle1 = Circle(5)
print(circle1.area())                # 78.53975

circle2 = Circle.from_diameter(10)
print(circle2.radius)                # 5.0

print(Circle.is_valid_radius(3))     # True