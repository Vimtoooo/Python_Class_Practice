# Classes can be referred to as a blueprint!
class MyClass:
    
    # Dunder method '__init__' will initialize an object for that class
    def __init__(self, name):
        self.name = name
    
    def greet(self) -> str:
        return f"Hello, I'm {self.name}"
    
    # This variable will be the class attribute
    emote: str = "dance"

class Student:

    school: str = "Python high school"

    def Name(self, name):
        self.name = name
    
    def Grade(self, grade):
        self.grade = grade

class Dog:
    def __init__(self, name, age = 1): # You can also have default values assigned to parameters in a method if the user has not inserted any!
        self.name = name
        self.age = age
    
    def info(self):
        return f"{self.name} is {self.age} years old."
    
class Calculator:
    def __init__(self):
        # TODO: Initialize the result attribute to 0
        self.result = 0

def my_decorator(func): # The parameter for the method which is applied with a different method can have any naming convention!
    def wrapper(*args, **kwargs):
        print("Before function runs")
        result = func(*args, **kwargs) # For example: func will represent the method which was nominated to become part of the decorator method!
        print("After function runs")
        return result
    return wrapper

class Greet:
    def __init__(self, name):
        self.name = name

    @my_decorator
    def say_hello(self): # Decorator method applied for this function from the my_decorator function
        print(f"Hello {self.name}")

class Circle:
    def __init__(self, radius):
        self._radius = radius # The underscore is just a naming convention and can be written in any way! (but not like the radius method!)

    @property
    def radius(self):
        return self._radius # Accesses the internal attributes...
    
    @property
    def area(self):
        return 3.14159 * pow(self._radius, 2)
    
    @radius.setter # @setter will set a new value for an attribute while being able to process some logic!
    def radius(self, value):
        if value > 0:
            self._radius = value # Now you can set the radius like an attribute!
        else:
            print("Radius must be positive!")

class Rectangle:

    def __init__(self, width: float | int, height: float | int):
        self._width = width
        self._height = height
    
    @property
    def width(self) -> float | int:
        return self._width

    @property
    def height(self) -> float | int:
        return self._height
    
    @width.setter
    def width(self, val): # KEY: Use name convention if there is a function/method with the same name as the attribute name!
        if val > 0:
            self._width = val
        else:
            print("Negative values are not allowed!")
    
    @height.setter
    def height(self, val):
        if val > 0:
            self._height = val
        else:
            print("Negative values are not allowed!")
    
    @property
    def perimeter(self) -> float | int:
        return 2 * (self._width + self._height)
    
class MathHelper:
    helper_name: str = "DeVoe"

    def __init__(self, name):
        self.name = name

    @staticmethod # The @staticmethod decorator does not modify class or instance data and does not require a 'self' parameter!
    def add(val1, val2) -> float | int:
        return val1 + val2
    
    @staticmethod
    def is_even(num: int) -> bool: # Useful for utility functions...
        return num % 2 == 0 # User: MathHelper.is_even(21) -> false
    
    # @staticmethod
    # def name_of_user(self): # This will raise a medium level problem...
    #     return self.name

class A_Student:
    school_name: str = "Python Academy"
    student_count: int = 0

    def __init__(self, name):
        self.name = name
        A_Student.student_count += 1
    
    @classmethod
    def get_school_info(cls):
        return f"School: {cls.school_name}, students: {cls.student_count}"
    
    @classmethod
    def create_guest_student(cls): # Use class methods as an alternative constructor!
        return cls("Guest")

class Library:
    total_books: int = 0

    def __init__(self, book):
        self.book = book # Instance attribute
        Library.total_books += 1 # Class attribute

    @classmethod
    def get_library_stats(cls):
        return cls.total_books
    

class The_Student:
    # Class variable / attribute - shared by all instances
    school = "Python High School"

    def __init__(self, name, grade):
        # Instance variables / attributes - unique to each student
        self.name = name
        self.grade = grade

class Person1:
    def __init__(self, name, age):
        self._name = name   # Protected - internal use
        self._age = age     # Protected - internal use

class Person:
    def __init__(self, name, age):
        self.__name = name   # "private" - gets name mangled
        self.__age = age     # "private" - gets name mangled
    
    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age must be positive!")

class Vehicle: # Parent class
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    @property
    def display_info(self):
        print(f"Vehicle: {self.make}, {self.model}")

class Car(Vehicle): # Child class (inherited from the Vehicle class)
    pass # But does not contain any attributes and methods

class University: # Parent class
    university_name: str = "Python University"
    num_of_students: int = 0
    
    def __init__(self, name: str):
        self.name = name
        University.num_of_students += 1
        print(f"Welcome to {University.university_name} {name}!")

    @classmethod
    def quantity_of_students(cls):
        print(f"Total number of students: {cls.num_of_students}")
    

class Students(University): # Child class
    
    def __init__(self, name: str, major: str):
        super().__init__(name) # Calls the parent's constructor method then extends it from where it stopped
        self._major = major
        print(F"Chosen major: {major}")
    
    @property
    def major(self):
        print(f"Major: {self._major}")
    
    @major.setter
    def change_major(self, new_major: str):
        
        if not new_major:
            print("Please enter a new major for the following student")
        else:
            self._major = new_major
            print("Major changed successfully!")

class Library1:
    
    num_of_books: int = 0

    def __init__(self, name: str):
        self.name: str = name
        self.num_of_books += 1
        print("Book registered successfully!")
    
    @property
    def info(self):
        print(f"Book name: {self.name}")

class Book(Library1): # Book class inherits from the Library1 class

    def __init__(self, name: str, literature: str):
        self.literature: str = literature
        super().__init__(name)

    @property
    def info(self):
        print(f"Book name: {self.name}")
        print(f"Literature type: {self.literature}") # This method overrides the parent's method but pursues the exact print statement with an extra one


class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"
    
class Flyable:
    def __init__(self, name):
        self.name = name
    
    def fly(self):
        return f"{self.name} is flying"
    
class Bird(Animal, Flyable): # Multiple inheritance
    def __init__(self, name, species):
        super().__init__(name)  # Calls Animal's __init__
        self.species = species
    
    def sing(self):
        return f"{self.name} is singing"
    

class Shape:
    @staticmethod
    def calculate_area() -> 0:
        return 0

class Rectangle(Shape):
    @staticmethod
    def calculate_area(n1: int | float, n2: int | float) -> int | float:
        return n1 * n2

class Triangle(Shape):
    @staticmethod
    def calculate_area(n1: int | float, n2: int | float) -> int | float:
        return (n1 * n2) / 2

# class Circle(Shape):
#     @staticmethod
#     def calculate_area(r): # These have been commented due to the example of the usage would not work for these classes in Main.py...
#         return 3.14 * pow(r, 2)

# class Parallelogram(Shape): # All child classes inherit from Shape but all override the parent's method
#     @staticmethod
#     def calculate_area(a, b, h):
#         return ((a + b) * h) / 2


class Horse:
    @property
    def walk(self):
        print("Walking like the western cowboy horses...")
    
    @property
    def sprint(self):
        print("Clop clop clop!")

class Human: # The Duck Typing approach signifies that polymorphism will be present, just without aay inheritance from any of the classes...
    @property
    def walk(self): # Both classes contain the same method names but with different print statements.
        print("Just a normal human being walking on the streets of the world...")

    @property
    def sprint(Self):
        print("Tip, tap, toe!")

from abc import ABC, abstractmethod # Import ABC and abstract method decorator for creating abstract classes

class Vehicle(ABC):
    @abstractmethod # Manipulate with the @abstractmethod decorator to mark methods that must be implemented to the subclasses
    def start_engine(self):
        pass # They are just for marking and not for utility, so we pass

    @abstractmethod
    def stop_engine(self):
        pass

    def honk(self):
        return "Honk!" # This is a concrete method, since it has implementations!

class Motorcycle(Vehicle): # Motorcycle (subclass/concrete class) inherits from Vehicle (abstract class)
    def __init__(self, model):
        self.model = model
    
    def start_engine(self): # This method overrides the start_engine from the parent class (abstract class)
        return "Nhaaaah!"

    # Notice how we have not created a concrete method for stop_engine
    # Because of this, we will not be able to instantiate from this subclass, we are missing a method definition called 'stop_engine'

class Car(Vehicle):
    def __init__(self, model):
        self.model = model
    @property
    def start_engine(self): # This subclass will have all correct and required implementations
        return "Brvuum!"

    def stop_engine(self):
        return "Engine stopped."

# Example 1 of Interface Design
class Playable(ABC): # We create an interface using abstract methods only
    
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Podcast(Playable): # Create a concrete class with all required implementations in the correct manner

    def __init__(self, name):
        self.name = name
    
    def play(self):
        return f"Playing {self.name}"
    
    def stop(self):
        return f"Stopping {self.name}"

# Example 2 of Interface Design
class Printable(ABC):
    
    @abstractmethod
    def print_document(self):
        pass

class PDFPrinter(Printable):
    def __init__(self, document):
        self.document = document
    
    def print_document(self):
        return f"Printing document in a PDF printer for: {self.document}"

class LaserPrinter(Printable):
    def __init__(self, document):
        self.document = document
    
    def print_document(self):
        return f"Printing document in a high quality graph for: {self.document}"
    

class BankAccount:
        
    # Local Scope Class Attributes
    interest = 0.02
    
    def __init__(self, account_holder, account_number):
        

        # Public Member Attributes
        self.account_holder = account_holder

        # Protected Member Attributes
        self._transaction_count = 0

        # Private Member Attributes
        self.__account_number = account_number
        self.__balance = 0
    
    
    def deposit(self, amount):
        
        if amount > 0:
            self.__balance += amount
            self._update_transaction_count
        else:
            print("Invalid input, please insert an appropriate value to deposit.")
    

    def withdraw(self, amount):
        
        if amount > 0:
            self.__balance -= amount
            self._update_transaction_count
        else:
            print("Invalid input, please insert an appropriate value to withdraw.")


    # Getter Methods
    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.account_holder

    # Protected Method
    @property
    def _update_transaction_count(self):
        self._transaction_count += 1
    
    @property
    def _calculate_interest(self):
        return self.__balance * BankAccount.interest
    
    # Private Method
    def __validate_transaction(self, amount) -> bool:
        return amount > 0 or amount >= self.__balance
    

# Applying dunder methods in a class
class Name:

    def __init__(self, name):
        self.name = name
    
    def change_name(self, new_name):
        self.name = new_name
    
    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)
    
