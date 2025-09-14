# Import an external file to begin manipulating with its code into your main file
from my_class import MyClass
import my_class

# Create an instance and use it
# my_object = MyClass("Vito")
# obj1 = MyClass("Bob")

# student1 = my_class.Student()
# student2 = my_class.Student()

# dog1 = my_class.Dog("Rex", 3)
# dog2 = my_class.Dog("Sven") # Age by default will be set to 1!

# calc = my_class.Calculator()

# name1 = my_class.Greet("Josh")

# circle1 = my_class.Circle(3)

# rect1 = my_class.Rectangle(4, 6)
# my_helper = my_class.MathHelper("Jack")

# alice = my_class.A_Student("Alice")
# bob = my_class.A_Student("Bob")

# lily = my_class.The_Student("Lily", "A")
# charlie = my_class.The_Student("Charlie", "B")

# Call the greet function to visualize your class object!
# print(my_object.greet())

# Check the type of the instance
# print(type(my_object))

# Call the class attribute
# print(MyClass.emote)
# print(my_object.emote)
# print(obj1.emote)
# print(calc.result)


# Create new attributes with existing class objects! (if not initialized)
# student1.name = "John"
# student1.grade = "C"
# print(student1.name, student1.grade)

# Call other methods in the class:
# print(dog1.info())


# Use decorators for improved code functionality!
# name1.say_hello()
# print(circle1.radius) # When a method utilizes a @property decorator, you don't need to use () when calling it!
# print(circle1.area)
# circle1.radius = 5 # Use the @setter
# print(circle1.radius) # Use the getter
# circle1.radius = -1 # Prints an error message
# print(circle1.radius)
# print(rect1.perimeter)
# print(my_class.MathHelper.add(2, 5))
# res = my_helper.is_even(7)
# print(res)
# info = my_class.A_Student.get_school_info() # Call class methods when using the class name
# print(info)
# updated_info = my_class.A_Student.get_school_info()
# print(updated_info)
# guest = my_class.A_Student.create_guest_student()
# print(guest.name)
# print(alice.get_school_info()) # Class methods can also be called from instances

# Access instance variables / attributes (unique to each other)
# print(lily.name, lily.grade)
# print(charlie.name, charlie.grade)

# Access class variables / attributes (shared by all objects)
# print(lily.school, charlie.school, my_class.The_Student.school)

# Now change the class variable
# my_class.The_Student.school = "Python Academy"
# print(my_class.The_Student.school)

# person = my_class.Person1("JJ", 21)
# print(person._name)

# person = my_class.Person2("Bob", 25)
# print(person.get_name())  # Bob

# person.set_age(30)
# person.set_age(-5)        # Age must be positive!

# person = my_class.Person("Charlie", 35)
# This doesn't work:
# print(person.__name)  # AttributeError

# But this works (discouraged): Raises a red error, but runs perfectly fine without crashing...
# print(person._Person__name)  # Charlie

# a_vehicle = my_class.Vehicle("Toyota", "Corolla") # Instance from the parent class
# a_car = my_class.Car("Honda", "Civic") # Instance from the child class (inherited from the Vehicle class)

# a_vehicle.display_info # Both will have access to attributes and methods from the parent class
# a_car.display_info

# university = my_class.University("Peter")

# student3 = my_class.Students("Jake", "Computer Science")
# my_class.University.quantity_of_students()
# student3.major
# student3.change_major = "Architecture"
# student3.major

# library = my_class.Library1("Comic book")
# hobbit = my_class.Book("Hobbit", "Fiction")

# library.info
# hobbit.info

# sparrow = my_class.Bird("Sparrow", "House sparrow")

# print(sparrow.eat())
# print(sparrow.fly())
# # print(sparrow.sing())
# print(my_class.Bird.__mro__) # Returns as a tuple
# print(my_class.Bird.mro()) # Returns as a list

# print(my_class.Bird.__name__) # returns Bird

# Basic Polymorphism in action!
# shape = my_class.Shape()
# rect = my_class.Rectangle()
# tri = my_class.Triangle()
# # cir = my_class.Circle()
# # par = my_class.Parallelogram()

# shapes: list[object] = [rect, tri]
# for s in shapes:
#     print(s.calculate_area(6, 7))

# horse = my_class.Horse()
# human = my_class.Human()

# def do_a_walk_and_sprint(instance: object):
#     # We utilized the @property methods for this example
#     instance.walk
#     instance.sprint

# do_a_walk_and_sprint(horse) # The duck typing will occur due to the same method names which have been applied to both class instances
# do_a_walk_and_sprint(human)

# Instantiate an instance from the subclass of Vehicle (subclass instance)
# bike = my_class.Motorcycle("bike") # Raises a TypeError since we have not defined a 'stop_engine' method with implementations...

# You cannot instantiate instances from an abstract class!
# vehicle = my_class.Vehicle() # Raiser an error during execution when instantiating abstract instances, which are not possible

# Create an instance from the Car class which contains all of the required methods
# car = my_class.Car("car")
# print(car.start_engine)
# print(car.stop_engine())

# First, we instantiate the instances from the concrete classes
# doc1 = my_class.PDFPrinter("doc1")
# doc2 = my_class.LaserPrinter("doc2")

# # Define a function to be able to print implemented methods which will be assigned to do one role (print the documents!)
# def exhibit_document(d: my_class.Printable): # Notice how we were able to type hint the interface class as a data type
#     print(d.print_document())

# # We can use the interface polymorphically with these different objects
# exhibit_document(doc1)
# exhibit_document(doc2)

# bank_account = my_class.BankAccount("Harry", 786465)
# print(bank_account.owner)
# bank_account.deposit(500)
# bank_account.deposit(1750)
# bank_account.withdraw(50)
# print(bank_account.balance)

# Test the dunder methods
# name1 = my_class.Name("Craig")
# print(name1) # calls __str__
# print(len(name1)) # Calls __len__
# name1.change_name("George")
# print(name1)

