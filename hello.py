
# class  in oop
class Car:
    def __init__(self,make, model, year, color):
        print(f"Creating a {color} {year} {make} {model}...")
        self.make = make
        self.model = model
        self.year = year
        self.color =color
        self.is_engine_on = False
        self.speed = 0
        
    def start_Engine(self):
        if not self.is_engine_on:
            self.is_engine_on = True
            print(f"The {self.model}'s engine is now on. Vroom!")
        else:
            print("The engine is already running.")
        
    def accelerate(self, amount):
        if self.is_engine_on:
            self.speed += amount
            print(f"Accelerating. The car is now moving at {self.speed} km/h.")
        else:
            print("You need to start the engine first!")
             
    def get_description(self):
        return f"This is a {self.color} {self.year} {self.make} {self.model}."
    


my_car = Car("Toyota", "Camry", 2021, "Blue")
your_car = Car("Honda", "Civic", 2022, "Red")


print(f"My car is a {my_car.make}.")
print(f"Your car is a {your_car.color} {your_car.model}.")

print("-" * 20)
my_car.start_Engine()
your_car.start_Engine() 

print("-" * 20)

my_car.accelerate(50)
your_car.accelerate(30)

print("-" * 20)

print(f"My car's speed: {my_car.speed} km/h")   # Output: My car's speed: 50 km/h
print(f"Your car's speed: {your_car.speed} km/h") # Output: Your car's speed: 30 km/h

print("-" * 20)


print(my_car.get_description())
print(your_car.get_description())


#A Real-World Example: The BankAccount 🏦

class BankAccount:
    
    def __init__(self,account_holder, initial_balance):
        self.account_holder = account_holder
        self.__balance = initial_balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance +=amount
            print(f"Deposited ${amount}. New balance is ${self.__balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.__balance}.")
    def get_balance(self):
        print(f"The current balance for {self.account_holder} is ${self.__balance}.")
        return self.__balance

my_account = BankAccount("John Doe", 1000)


my_account.get_balance()
my_account.deposit(1000)
my_account.withdraw(2000)
my_account.get_balance()
my_account.deposit(-50)
my_account.withdraw(5000)

print("\n--- The WRONG way (trying to bypass encapsulation) ---")
try:
    my_account.__balace = 500000
    print("Balance was changed directly!")
    print(my_account.account_holder)
except AttributeError  as e:
    print(f"Failed to access private attribute: {e}")
print("\nFinal balance check:")
my_account.get_balance()
            
#abstraction

from abc import ABC,abstractmethod
import math
class Shape(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def area(self):
        pass
    def who_am_i(self):
        print(f"I am a {self.name}.")
    
class reactangle(Shape):
    def __init__(self, name,length,width):
        super().__init__(name)
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2 )

my_rect = reactangle("Ractangle",5,5)
my_circle = Circle("Circle",5)

my_rect.who_am_i()
print(f"Area of rectangle is :{my_rect.area()}")

my_circle.who_am_i()
print(f"Area of Circle is :{my_circle.area() :.2f}")


class Dog:
    def speak(self):
        return "Woof! Woof!"

class Cat:
    def speak(self):
        return "Meow..."

# Let's add another class that is completely unrelated to Animals
class Car:
    def speak(self):
        return "Honk! Honk!"

# --- The Polymorphic Part ---

# This function doesn't know or care what type of object it gets.
# It only cares that the object has a .speak() method.
def make_it_speak(thing):
    print(thing.speak())


# Create different objects from different classes
dog = Dog()
cat = Cat()
car = Car()

# Call the same function with different types of objects
print("Calling the function with a Dog object:")
make_it_speak(dog)

print("\nCalling the function with a Cat object:")
make_it_speak(cat)

print("\nCalling the function with a Car object:")
make_it_speak(car)


class Car:
    total_cars_made = 0 # This is a class attribute

    def __init__(self, make, model):
        self.make = make    # Instance attribute
        self.model = model  # Instance attribute
        Car.total_cars_made += 1

    # An instance method: works with a specific car instance (self)
    def display_info(self):
        print(f"This is a {self.make} {self.model}.")

    # A class method: works with the class itself (cls)
    @classmethod
    def get_total_cars_made(cls):
        print(f"Total cars made by this factory: {cls.total_cars_made}.")

    # A static method: a related utility function, doesn't use self or cls
    @staticmethod
    def is_valid_vin(vin_number):
        return len(vin_number) == 17

# --- Usage ---
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

car1.display_info() # Calling an instance method
Car.get_total_cars_made() # Calling a class method

# Calling a static method
print(f"Is VIN '123' valid? {Car.is_valid_vin('123')}")
print(f"Is VIN '12345678901234567' valid? {Car.is_valid_vin('12345678901234567')}")


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # The __str__ method is called by print() and str()
    # It should return a user-friendly string.
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # The __len__ method is called by len()
    def __len__(self):
        return self.pages

    # The __add__ method is called by the + operator
    def __add__(self, other_book):
        # Let's say adding two books creates a "Book Series"
        return f"Book Series: [{self.title}, {other_book.title}]"

# --- Usage ---
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1178)

# 1. Using __str__
print("--- Using print() on the object ---")
print(book1) # Python secretly calls book1.__str__()

# 2. Using __len__
print("\n--- Using len() on the object ---")
print(f"The book has {len(book1)} pages.") # Python calls book1.__len__()

# 3. Using __add__
print("\n--- Using the + operator on objects ---")
series = book1 + book2 # Python calls book1.__add__(book2)
print(series)