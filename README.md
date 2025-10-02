# NOTES: Object Oriented Programming Basics

External files in python allow you to access classes and defined functions that already exist in a different file that you would like to utilize for other files, when importing, simply just mention the name of the file after the import keyword and you will now have access to everything that the mentioned file has to offer!

- **Classes are referred to as blueprints**, while **objects are what you build from that blueprint!**;
- Once a class attribute (variable) is created, **all objects/instances** will have access to the attributes, ex: **obj.class_attribute**;
- Objects can have individual attributes that classes cannot, ex: **Classes:** class.attribute, **Objects:** obj.attribute, obj.new_attribute = element (creating a new attribute);
- The **self** parameter refers to the instance of a class within methods! (self parameter must **ALWAYS** be the first parameter in method definitions);
- The self parameter lets each object access its own data, without self, methods won't know which object's attributes to use (class.method() is equal to object.method());

### Methods can:

- Take parameters like add(self, a, b);
- Return values like return a + b;
- Print out directly like print("Hello!");
- And do both printing and returning;

## Attributes:

Attributes are local scope variables or data that belong to a class or its objects, they store information about the object's state. There are two types of attributes.

### **Class Attributes:**

Shared by all objects of the class, ex: You defined a class called `Student` with a local scope variable located inside the class called `school_name` = "Python School" (not inside any defined functions!);

### **Object/Instance Attributes:**

They are unique to each other, ex: Inside the `Student` class where there will be a defined function/method called `set_info` that takes `self` (the object/instance), `name` and `age` as its parameters, defined to set a value to the objects or attributes by declaring with self.name = name and self.age = age.

**KEY DIFFERENCE:** Class attributes are shared by all objects, while object/instance attributes are unique to each object, use:

- `self.attribute_name` for instance attributes;
- `class.attribute_name` or `object.attribute_name` for class attributes.

### The Constructor/Dunder Method (\***\*init\*\***):

The infamous dunder method called `__init__` is a special method that automatically runs when you create an object, it initializes the object's attributes.
Here is an example of a class with a constructor: (check my_class.py at line 25 - 27)

- `__init__` takes parameters and assigns them to instance attributes using `self`;
- Create objects using the constructor: object = Class("element1", element2);
- After that, Python will automatically call the `__init__` method and pass the argumemts to the instance's attributes;
- You can also assign a constructor with default values, example at line 25 at my_class.py.

**KEY POINT:** The `__init__` method ensures every object is properly set up with its initial data. It save you from manually setting attributes after object creation.

## Decorators:

### What are Decorators?

Decorators are a way to modify or enhance functions and classes without changing their original line of code, where they utilize the **@** symbol.
Here is an example of a simple decorator located at lines 37 - 51 in my_class.py:

### `@my_decorator`:

- Decorators make your code more readable and cleaner for your classes files;
- Decorators are applied with `@decorator_name` syntax above the function definition, knowing that they should accept and return functions;
- If you were to use decorators, they must be located above and outside the defined class;
- **Always manipulate your wrappers** with the `*args` and `**kwargs` parameters to support any arguments;
- It is best practice to keep your decorators in your classes files to be able to reuse it across multiple files, this also keeps your code organized and modular;
- For **large projects** with many decorators, you should consider storing all decorators in a **decorators.py** file for arranging all your code.

**KEY POINT:** Decorators wrap around functions to add extra functionality without modifying the original function code!

### `@Property` & `@Setter` Decorators:

The `@property` decorator allows you to access methods like attributes, providing a clean way to get and set values. Here is an example at lines 54 - 71 at my_class.py and object attribution examples at Main.py.

- `@property`: Decorators can be assigned to any method/function, making it a **read-only attribute**, meaning that you can access methods like an attribute, without needing parentheses!;
- **Encapsulation:** They allow you to control access to private attributes while still providing a simple interface;
- **Readability:** You can use methods as if they were attributes, making your code cleaner and more intuitive;
- **Validation:** You can add logic to get (and set with `@property_name.setter`) attribute values such as validation or computation, without changing how the attribute is accessed;
- `@property_name.setter`: Allows the user to change values and get values (see at lines 58 - 71) incremented with validation and logic (depending on the user's choice);
- Putting an underscore before naming the instance attribute in the format **self.\_attribute_name** is a **naming convention** that indicates the the attribute is intended to be private (for internal use only), which helps distinguish between the internal attribute (\_attribute_name) and the public property (attribute), but the attribute name can be written in any way, this simply indicates that certain data should not be accessed directly from outside the class.

**KEY POINTS:** `@property`makes methods look like attributes while `@property_name.setter` allows you to control how values are assigned. Also, use name conventions if there is a function/method with the same name as the attribute name to prevent recursion errors! (example at lines between 80 - 103 in my_class.py). A simple underscore as a prefix for the instance attribute will solve the problem...

### `@staticmethod` Decorators:

Next in the list is the `@staticmethod` decorator, which creates methods that don't require the use of the `self` parameter or the class itself. They work like regular functions but belonging to classes. See examples in my_class.py (lines 105 - 117) and usages at Main.py (pages 22, 54 - 56)...

- The method does not take `self` or the class as its first parameter;
- They **do not access or modify the class or instance (object) itself**, behaving like a regular function, but grouped logically inside the class;
- **Why use @staticmethod?** It organizes utility methods that are related to the class or instance data, making your code more readable and maintainable;
- You can call static methods with the class name or from the instance, for example: Class_name;method_name(`parameter`, ... ) OR object_name.method_name(`parameters`, ... ), these examples can also be seen at lines 54 - 56 in Main.py;
- Trying to add `self` as a parameter in a method with the `@staticmethod` with raise a medium level type of error, which should be considered to be fixed.

**KEY POINTS:** You should consider wielding with the `@staticmethod` decorator only when you need a function that is related to the class, but doesn't need access to an instance (the parameter `self`) or class data. No self parameter needed!

### `@classmethod` Decorators:

The `@classmethod` decorators create methods that receive the class itself (the parameter `cls`) as the first parameter instead of the instance/object `self`. Examples at lines 123 - 137 at my_class.py.

- They are used to define a method that receives the **class itself** instead of the instance `self` as the first argument, usually named `cls` (first parameter is always `cls` (the class), not `self` (the instance));
- You can call a class method on the class and treat it like a class attribute or on an instance;
- Useful for factory methods, alternative constructors, or when you need to work with class variable (class attributed).

**KEY POINT:** Operate with `@classmethod` when you need to access class attributes or create alternative ways to construct objects (to create a `Class_name` object), the first parameter is `cls` (the class itself), not `self` (the object or instance).

**REMEMBER:** If you attempt to combine the `@property` and `@classmethod` decorators in a single method, there will appear a strikethrough in your method because both of these decorators in one method are **not supported in standard Python**, since the `@property` decorator is exclusively made for **attributes methods** while the `@classmethod` property is for **class methods**, allowing you to call them in the class itself. But when you stack both of these decorators, Python does not provide a built-in way to create a 'class property' that you can access as `Class_Name.attribute` without calling it.

## Class Properties:

### Instance Vs Class Variables:

Instance objects are unique to each object, while local scope class variables are shared by all objects of the same class. Here are a few examples of usage between lines 72 - 81 at Main.py and lines 150 - 157 in my_class.py file:

#### Pros and Cons of **class attributes** and **instance attributes**:

|   Attribute Type    | Shared? | Unique? | Memory Efficient? | Easy Global Update? | Risk of Side Effects? |
| :-----------------: | ------- | ------- | ----------------- | ------------------- | --------------------- |
|  Class Attributes   | Yes     | No      | Yes               | Yes                 | Yes (if mutable)      |
| Instance Attributes | No      | Yes     | No                | No                  | No                    |

**KEY DIFFERENCE:** Instance variables (created with self.variable_name) are unique to each object, while class variables (defined directly in the class) are shared by all objects, changing a class variable will affect all instances.

#### **BEST PRACTICE:**

- Use **class attributes** for data shared by all instances (constants, counters, ... );
- Use **instance attributes** for data that are unique to each other.

### Private attributes:

Private attributes are **underscores** that are **connected with the attrubute** indicating that specific data should not be accessed directly from **outside the class**. Here are a few examples: (lines 159 - 176 in my_class.py)

#### Single underscores:

```json
class Person:
    def __init__(self, name, age):
        self._name = name       # "Protected" - internal use
        self._age = age         # "Protected" - internal use
```

Remember that single underscore attributes can still be accessed, but it's a signal not to.

```json
person = Person("Alice", 30)
print(person._name)     # Works, but not recommended
```

#### Double underscores:

Use double underscores for stronger privacy (name mangling):

```json
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
```

Use the accessor methods to interact with private attributes:

```json
person = Person("Bob", 25)
print(person.get_name())  # Bob

person.set_age(30)
person.set_age(-5)        # Age must be positive!
```

Double underscore attributes get "name mangled" but can still be accessed:

```json
person = Person("Charlie", 35)
# This doesn't work:
# print(person.__name)  # AttributeError

# But this works (discouraged): Raises a red error, but runs perfectly fine without crashing...
print(person._Person__name)  # Charlie
```

**KEY POINT:** Single underscore `_attribute` means "internal use only", double underscores `__attribute` triggers name mangling for stronger privacy. Use accessor methods to properly interact with private data and add validation.

## Inheritance:

Inheritance allows a class to inherit attributes and methods from another class, creating a parent-child relationship. Here is an example of a parent class: More examples in my_class.py between lines 178 - 188 and use of objects in Main.py in lines 99 - 103.

### Basic Inheritance:

```json
class Animal:  # Here, we have the primary class called `Animal` (parent class), which includes a constructor and an info method...
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"I am {self.name}, an animal")
```

Then, we create another class called `Dog` that inherits from the previous class, becoming the child class (`Animal`, which will represent the **parent** class):

```json
class Dog(Animal):
    pass  # Inherits everything from Animal
```

The syntax `class Dog(Animal):` means that `Dog` inherits from `Animal`, and always put the parent class inside the parentheses!
Next, we create instances from both classes and wield with the inherited methods:

```json
generic_animal = Animal("Creature")
buddy = Dog("Buddy")

generic_animal.info() # -> I am Creature, an animal
buddy.info() # -> I am Buddy, an animal
```

Even though `Dog` doesn't define a constructor method `__init__` or `info`, it automatically gets them from the `Animal` class. We can even add more methods into the child class `Dog`:

```json
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

buddy = Dog("Buddy")
buddy.info()  # Inherited method
buddy.bark()  # New method

# Output:
# I am Buddy, an animal
# Buddy says Woof!
```

**\*KEY POINT:** Child classes inherit all attributes and methods from their parent class, use the `class Child_class(Parent_class):` syntax to create inheritance, this helps you reuse code and create logical class hierarchies.

### The `super()` function:

The `super()` function allows a child class to call methods from its parent class, which lets you extend parent functionality rather than completely replacing it. Here are the following examples:

```json
class Animal:
    def __init__(self, name): # We will call the super() function and link it to the parent's constructor method to extend its current code functionality!
        self.name = name
        print(f"Animal created: {name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # Call the parent's __init__ method
        self.breed = breed
        print(f"Dog breed set: {breed}")

# Create a Dog object:
buddy = Dog("Buddy", "Golden Retriever")
print(f"Name: {buddy.name}, Breed: {buddy.breed}")

# Output:
Animal created: Buddy
Dog breed set: Golden Retriever
Name: Buddy, Breed: Golden Retriever
```

Utilize `super()` to avail oneself of the parent methods for further extension!

```json
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()  # Call parent's make_sound() method first
        print("Woof!")        # Add dog-specific behavior

buddy = Dog("Buddy", "Golden Retriever")
buddy.make_sound()

# Output:
Generic animal sound
Woof!
```

#### Why use the `super()` function?

Without the `super()` function, you would **loose the parent's functionality**, only calling methods which would be **located locally inside the child class**, but simultaneously still having access to nearly all of the parent class methods (only if the parent's method does not have an **identical name** to the child's method!).

```json
class Cat(Animal):
    def make_sound(self):
        print("Meow!")  # Only cat sound, parent method ignored

cat = Cat("Whiskers")
cat.make_sound()

# Output:
Meow!
```

**KEY POINT:** Use `super()` to call specific parent class methods from the child classes. This allows you to extend functionality rather than completely replacing it. Common uses include calling parent `__init__` methods and extending parent behavior. More examples can be located in the my_class.py file between lines 190 - 222 and in Main.py at lines 105 - 111 for examples of usage.

### Method Overriding:

Method overriding allows the a child class to provide its own implementation of a method that already exists in the parent class. Here is an example of a parent class with methods and a child class that encompasses one method that pursues the exact method name as the parent's method:
(Examples in my_class.py file between lines 224 - 246 and in Main.py 113 - 117)

```json
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some generic animal sound")

    def info(self):
        print(f"I am {self.name}")

# Create a child class that overrides one method
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")  # Override the parent method
```

The `make_sound` methods in `Dog` replaces the one from `Animal`, but `info` is still inherited unchanged. Now, we'll create instances and test the methods:

```json
animal = Animal("Generic Animal")
dog = Dog("Buddy")

# Call the overridden methods
animal.make_sound()
dog.make_sound()

# Call the none-overridden methods
animal.make_sound()
dog.make_sound()

# Output:
Some generic animal sound
Woof! Woof!
I am Generic Animal
I am Buddy
```

You can override **any inherited method**, depending on how you would like your program to function and what to stimulate.

```json
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

    def info(self):
        print(f"I am {self.name}, a sneaky cat")

cat = Cat("Whiskers")
cat.make_sound()
cat.info()

# Output:
Meow!
I am Whiskers, a sneaky cat
```

**KEY POINT:** Method overriding lets child classes customize inherited behavior, simply **define a method with the same name in the child class**, the child's version will be utilized instead of the parent's version. But in the over hand, if you want to give preference for the parent's method, **always manipulate with the `super()` function** so that you can call methods directly from the parent's class!

### Multiple Inheritance:

Multiple inheritance allows a class to inherit from more than one parent class simultaneously, combining functionality from different sources. (More at my_class.py lines 249 - 269 and appliance in Main.py lines 119 - 124)
Below are the examples:

```json
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

class Flyable:
    def fly(self):
        return f"{self.name} is flying"

# Create a child class that inherits from both classes
class Bird(Animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)  # Calls Animal's __init__
        self.species = species

    def sing(self):
        return f"{self.name} is singing"
```

The syntax `class Bird(Animal, Flyable):` means that the `bird` class (child class) inherits from both `Animal` and `Flyable` classes (both becoming parent classes). Let us make some experiments!

```json
sparrow = Bird("Sparrow", "House sparrow")
print(sparrow.eat())
print(sparrow.fly())
print(sparrow.sing())

# You can check the inheritance order using either the __mro__ dunder method or the mro() function
print(Bird.__mro__)  # Method Resolution Order

# Output:
Sparrow is eating
Sparrow is flying
Sparrow is singing
(<class 'my_class.Bird'>, <class 'my_class.Animal'>, <class 'my_class.Flyable'>, <class 'object'>)
# As you can see, the MRO order begins from the Bird class (child class), then goes to Animal (primary parent class), then to Flyable (secondary parent class) and finally to the object itself!
```

The `__mro__` or the `mro()` method and function check whether which parent gets checked first when looking for methods...

**IMPORTANT:** Similar to `if` and `else` statements, Python uses the **Method Resolution Order (MRO)** to determine which parent class’s method is called when you use super() or when you access an attribute/method. Depending on how you want your code to function, it is key to consider the order of your inherited classes, the first inherited class will always be the first to be scanned for particular methods that the user tries to call. This could also impact the efficiency of your program and be mindful of what parent classes should be nominated to be the primary, secondary, tertiary and so on.

**KEY POINT:** Multiple inheritance uses the `class Child_Class(Parent1, Parent2):` syntax, where the child class obtains all of the methods from all parent classes, Python checks parent classes from left to right when looking for methods or attributes.

### Method Resolution Order (MRO):

Method Resolution Order (MRO) is a sequence that Python operates to look for methods when multiple classes have the exact same method name, here is an example of multiple classes having the same method name:

```json
class A:
    def method(self):
        return "Method from A"

class B:
    def method(self):
        return "Method from B"

class C(A, B):
    pass

# Check the MRO using __mro__ to return it as a tuple or mro() to return it as a list
print(C.__mro__)

# Output:
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
```

This shows Python will check `C` first, then `A`, then `B`, then the built-in object class.

```json
# Create an object then call the method
c = C()
print(c.method())

# Output:
Method from A
```

Python found the method in class `A` first, so it made use of it. Now, let's change the inheritance order to see the difference:

```json
class D(B, A):  # B comes before A now
    pass

print(D.__mro__)
d = D()
print(d.method())

# Output:
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
Method from B
```

So Python finds B's method first because `B` come before `A` in the inheritance list.

**IMPORTANT:** The `__mro__` and `mro()` methods can only be assigned to the class name and not instances. Also keep in mind that the `__mro__` method returns the order inside a tuple, while the `mro()` returns in a list!

**KEY POINT:** Python searches for **methods in MRO order**, the class itself first, then the inherited parent classes from left to right as listed in the class definition, the first method found gets used. Use `__name__` to get the name of the class and not the type!

## Polymorphism:

Polymorphism means "many forms" and allows objects of different classes to respond differently to the same method call. Method overriding makes this possible.

### Method Overriding Revisited:

Here is a parent class with a method, where all of the child classes will also contain their own knock-off versions of the same method name:

```json
# Parent class
class Animal:
    def speak(self):
        return "Animal makes a sound"

# Child classes
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"
```

Each class provides its own implementation of the method `speak()`, let's create a list of different animals!

```json
animals = [Dog(), Cat(), Cow(), Animal()]

# Call the same method on ALL OBJECTS
for animal in animals:
    print(animal.speak())

# Output:
Woof!
Meow!
Moo!
Animal makes a sound#
```

This is essentially **polymorphism in action** - the same method call behaves differently in based on the object's actual type, you can also utilize polymorphism with functions:

```json
def make_animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Woof!
make_animal_speak(cat)  # Meow!
```

The function doesn't have to know what type of animal it receives, it just calls `speak()` and gets the right behavior.

**KEY POINT:** Polymorphism lets you treat different objects the same way through a common interface. Method overriding provides different implementations, while polymorphism lets you call them uniformly. This make your code more flexible and easier to read.

More examples of polymorphism in lines 272 - 285 in my_class.py and usage in lines 129 - 138 in Main.py.

### Duck Typing:

Duck typing focuses on what an object can do, not what it is. If an object has the methods you need, you can use it - regardless of its class type. Here are two unrelated classes with the same methods:

```json
class Duck:
    def swim(self):
        return "Duck swimming"

    def quack(self):
        return "Quack!"

class Person:
    def swim(self):
        return "Person swimming"

    def quack(self):
        return "Person imitating a duck: Quack!"
```

Notice that `Person` and `Duck` don't inherit from the same parent class, but they both have `swim()` and `quack()` methods. Let's create a function that works with any "duck-like" object:

```json
def make_it_swim_and_quack(duck_like_object):
    print(duck_like_object.swim())
    print(duck_like_object.quack())

# This function doesn't care about the object's type - it only cares that the object has the required methods!
# Use the function with both classes:
make_it_swim_and_quack(Duck())
make_it_swim_and_quack(Person())

# Output:
Duck swimming
Quack!
Person swimming
Person imitating a duck: Quack!
```

We can also add another "duck-like" class in the mix:

```json
class Robot:
    def swim(self):
        return "Robot swimming with propellers"

    def quack(self):
        return "Robot sound: BEEP BEEP!"

make_it_swim_and_quack(Robot())

# Output:
Robot swimming with propellers
Robot sound: BEEP BEEP!
```

**KEY POINT:** Duck typing allows polymorphism **without inheritance**, if the object has the methods you need, you can use it!
This makes Python code flexible and follows the principle: "It's easier to ask forgiveness than permission,"

See more examples of Duck Typing in lines 298 - 314 in my_class.py and usage in lines 140 - 149 in Main.py.

### Abstract Classes and Methods:

Abstract classes are classes that cannot be instantiated directly and contain abstract methods that must be implemented by subclasses. Python provides the `abc` module for abstract base classes, **import the `abc` module to create abstract classes and utilize the `@abstractmethod` decorator**:

```json
from abc import ABC, abstractmethod

# Then create an abstract class with abstract methods
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return "This is a shape"  # Concrete method (has implementation)
```

The `@abstractmethod` decorator **marks methods that must be implemented by subclasses**, regular methods like `describe()` can have implementations. However, if you try to create an instance of the abstract class, Python will not allow this type of action to happen.

```json
# This will cause an error:
shape = Shape()  # TypeError: Can't instantiate abstract class
```

Let's create a concrete subclass (child class) that implements all of the abstract methods from `Shape`:

```json
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self): # Both area and perimeter methods override the abstract class's methods
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Now you can create instances from the concrete class (Circle):
circle = Circle(5)
print(circle.area())
print(circle.perimeter())
print(circle.describe())  # Inherited concrete method

# Output:
78.5
31.400000000000002
This is a shape
```

We can create another concrete subclass by operating with the same abstract class:

```json
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(4, 6)
print(rectangle.area())
print(rectangle.perimeter())

# Output:
24
20
```

**REMEMBER: You cannot instantiate abstract classes to instances/objects!** But also, a class will or method will only be called a concrete class/method if it provides implementation.

**KEY POINT:** Abstract classes define a template that subclasses classes (child classes) must follow. Always wield with the `ABC` module and `@abstractmethod` decorator to create abstract classes. **subclasses must implement all abstract methods, or they will also be abstract.**

More examples of Abstract methods and classes in my_class.py lines 16 - 348 and usage in Main.py lines 151 - 160.

### Interface Design:

An interface defines a contract that classes must follow. In Python, we create interfaces using abstract base classes where all methods are abstract. Follow down below for an example:

```json
# Import the abc module
from abc import ABC, abstractmethod

# Create an interface using abstract methods only
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, width, height):
        pass
```

In interface design, all methods in an interface should be abstract - they define what implementing classes must do, not how to do it!

Now, let's implement the interface in a concrete class (the subclass which will pursue implementation to be overridden from the abstract class Drawable):

```json
class Circle(Drawable): # Inherits from the abstract class Drawable (all abstract methods inside that class must be implemented in a correct manner into the concrete class)...
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        return "Drawing a circle"

    def resize(self, width, height):
        self.radius = min(width, height) / 2
        return f"Resized circle to radius {self.radius}"

# Create another concrete class that implements the same interface
class Rectangle(Drawable):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        return "Drawing a rectangle"

    def resize(self, width, height):
        self.width = width
        self.height = height
        return f"Resized rectangle to {width}x{height}"

# Use the interface polymorphically
shapes: list[object] = [Circle(5), Rectangle(3, 4)]

for shape in shapes:
    print(shape.draw())
    print(shape.resize(10, 8))

# Output:
Drawing a circle
Resized circle to radius 4.0
Drawing a rectangle
Resized rectangle to 10x8
```

You can also use interfaces as type hints (for type hinting a particular class, mention it exactly like it after the colon, ex: def Runner(p: Player) the parameter can be named any way, but the type hint is more strict):

```json
def render_shape(drawable: Drawable):
    return drawable.draw()

circle = Circle(3)
print(render_shape(circle))

# Output:
Drawing a circle
```

**KEY POINT:** Interfaces define **what classes must do, not how they do it.** Use abstract base classes with**only abstract methods to create clear contracts that implementing classes must follow**, this ensures consistent behavior across different implementations.

Check out more examples in my_class.py lines 350 - 391 and usage in Main.py lines 162 - 172.

## Encapsulation:

Encapsulation in Object-Oriented Programming (OOP), as implemented in Python, refers to the bundling of data (attributes) and the methods (functions) that operate on that data into a single unit, known as a class. It also involves restricting direct access to some of an object's components, promoting data security and integrity.

### Public, Protected and Private Members:

Python has three types of access controls for class members, where these control how attributes and methods can be accessed:

- **Public:** - Can be accessed from anywhere (inside or outside the class), where methods and attributes can be used freely, syntax of an underscore prefix. For example: `self.name`.

```json
class Person:
    def __init__(self, name):
        self.name = name  # public

p = Person("Alice")
print(p.name)  # Accessible
```

- **Protected:** - Should be accessed only within the class and its subclasses (not enforced, just a convention), which indicates for "internal use" of "protected" data, not part of the public API, syntax of a single underscore prefix. For example: `self._age`.

```json
class Person:
    def __init__(self, name, age):
        self._age = age  # protected

class Student(Person):
    def get_age(self):
        return self._age  # Accessible in subclass

s = Student("Bob", 20)
print(s._age)  # Technically accessible, but discouraged
print(s.get_age()) # Recommended way to obtain protected attributes through a class method in a subclass
```

- **Private:** - Gets the "name-mangled" to prevent direct access from outside the class (which the syntax of `_ClassName__attribute`), which pursues a stronger privacy for methods and attributes that should not be accessed outside the class, syntax of double underscore prefix. For example: `self.__salary`.

```json
class Person:
    def __init__(self, salary):
        self.__salary = salary  # private

    def get_salary(self):
        return self.__salary

p = Person(5000)
# print(p.__salary)  # AttributeError
print(p._Person__salary)  # Accessible, but discouraged
print(p.get_salary()) # Also returns the private attribute in a simpler manner through a public method provided by the class (recommended)
```

Now, here is an example of a class with all three access levels:

```json
class BankAccount:
    def __init__(self, owner, balance, account_id):
        self.owner = owner           # Public - accessible anywhere
        self._balance = balance      # Protected - internal use
        self.__account_id = account_id  # Private - class only

    def deposit(self, amount):       # Public methods
        self._balance += amount

    def get_account_id(self):
        return self.__account_id

    def _calculate_interest(self):   # Protected method
        return self._balance * 0.02

    def __validate_transaction(self, amount):  # Private method
        return amount > 0 and amount <= self._balance


# Access Public members from anywhere!
account = BankAccount("Alice", 1000, "12345")
print(account.owner)        # Alice
account.deposit(500)        # Works fine

# Access Protected members (single underscore - convention only):
print(account._balance)     # 1500 - works but not recommended
result = account._calculate_interest()  # Works but not recommended
print(result)               # 30.0

# Try to access private members (double underscore - name mangled):
# This won't work:
# print(account.__account_id)  # AttributeError

# But this works (name mangling):
print(account._BankAccount__account_id)  # 12345
```

If you want to access protected or private attributes, always define a method that returns that attribute in the correct syntax!
Create a subclass to show protected vs private access:

```json
class SavingsAccount(BankAccount):
    def show_balance(self):
        return self._balance        # Protected - accessible in subclass

    def show_id(self):
        # return self.__account_id  # This won't work - private
        return "Cannot access private member" # Instead, a string will be returned back to the user

        # Recommended way:
        # return self.get_account_id() # Safer and it preserves encapsulation

savings = SavingsAccount("Bob", 2000, "67890")
print(savings.show_balance())  # 2000
print(savings.show_id())       # Cannot access private member

# Output from all declarations:
Alice
30.0
30.0
5000
5000
Alice
1500
30.0
12345
2000
Cannot access private member
```

**REMEMBER:** Python's access controls are based on naming conventions, not strict enforcement.Use them to signal your intent and help others use your classes correctly. Also, using the syntax for getting a private attribute `obj._ClassName__attribute` is **discouraged** because it **breaks encapsulation!** Use a getter method to safely access private data, as it preserves encapsulation and allows for validation or logic inside the method. Note that **protected attributes** can be accessed using **any getter method in parent or subclasses**, while **private attributes** can only be returned in the **parent class (origin of creation)**.

**KEY POINT:** Key Point: Public members have no prefix and are accessible anywhere. Protected members use single underscore (\_) and should only be used within the class hierarchy. Private members use double underscore (\_\_) and are name-mangled for stronger privacy to prevent accidental access from outside the class. Python's access control is convention-based, not strictly enforced.

#### Summary Table:

|     Type      | Syntax   | Access Level              | Purpose                              |
| :-----------: | -------- | ------------------------- | ------------------------------------ |
|  **Public**   | `name`   | Anywhere                  | For general usage                    |
| **Protected** | `_name`  | Class & subclasses        | Internal use and for subclass access |
|  **Private**  | `__name` | Class only (name mangled) | Strong privacy, internal logic       |

See examples in file practice.py lines 510 - 626.

### Access Modifiers:

Access modifiers control the visibility of class attributes and methods. Python uses naming conventions rather than keywords for access control. Here are a few examples:

#### Public Access (no prefix):

```json
class Person:
    def __init__(self):
        self.name = "Coddy"      # Public attribute

    def greet(self):             # Public method
        return f"Hello, I'm {self.name}"

# We can access public members from anywhere
person = Person()
print(person.name)           # Coddy
print(person.greet())        # Hello, I'm Coddy
```

#### Protected Access (single underscore):

```json
class Employee:
    def __init__(self):
        self._salary = 50000     # Protected attribute

    def _calculate_bonus(self):  # Protected method
        return self._salary * 0.1

    def show_bonus(self):
        return self._calculate_bonus()  # OK to use within class

# Access protected members (works but not recommended)
employee = Employee()
print(employee._salary)      # 50000 - works but discouraged
print(employee.show_bonus()) # 5000.0 - proper way (for internal use within the class)
```

#### Private Access (double underscore):

```json
class User:
    def __init__(self):
        self.__password = "secure123"   # Private attribute

    def __encrypt(self, data):          # Private method
        return f"Encrypted: {data}"

    def verify(self, input_password):
        # Private members accessible inside the class
        return input_password == self.__password

# Use private members correctly
user = User()
print(user.verify("secure123"))  # True - using public method
# print(user.__password)         # AttributeError - cannot access directly

# Outputs:
Coddy
Hello, I'm Coddy
50000
5000.0
True
```

**KEY POINT:** Access modifiers are naming conventions where:

- No Prefix = Public (accessible anywhere);
- Single Underscore = Protected (internal use);
- Double underscore = Private (used within the origin class only).

These help establish clear boundaries and prevent accidental misuse of class internals.

### Information Hiding:

Information hiding restricts direct access to object components, requiring all interactions to occur through well-defined interfaces. This protects internal data from unauthorized access. We will illustrate a class with different levels of information hiding:

```json
class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner                    # Public - can be accessed directly
        self._balance = initial_balance       # Protected - internal use
        self.__account_number = "ACC123456"   # Private - hidden from outside

    # Add methods that provide controlled access to hidden data
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance: # If amount is greater than 0 and less or equal to the current balance
            self._balance -= amount
            return True
        return False

    def get_balance(self):
        return self._balance

    def get_account_info(self):
        # Safe way to show partial private data
        return f"Owner: {self.owner}, Account: ***{self.__account_number[-4:]}"

# Use the class through its public interface
account = BankAccount("Alice", 1000) # Initialize an instance with storing values for the attributes

# Access public data directly
print(account.owner)  # Alice - public access OK

# Use controlled methods for returning protected data
print(account.get_balance())  # 1000 - controlled access
account.deposit(500)
print(account.get_balance())  # 1500 - balance changed safely

# Try to access hidden data
print(account.get_account_info())  # Owner: Alice, Account: ***3456
# print(account.__account_number)  # AttributeError - hidden (use _ClassName__Attribute but its discouraged to do so!)

# The private attribute is name-mangled but still technically accessible
# This works but violates information hiding:
print(account._BankAccount__account_number)  # ACC123456


# Output:
Alice
1000
1500
Owner: Alice, Account: ***3456
ACC123456
```

**KEY POINT:** Information hiding protects internal data by making it **private** or **protected**, then providing controlled access through public methods. This prevent direct manipulation of sensitive data and ensures data integrity through validation in the access methods.

### Advanced Property Decorators:

Advanced property decorators provide more sophisticated control over attribute access, including computed properties, deleters and full property management. Here is an example of computed properties that derive values from other attributes:

```json
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Two getter methods that return different values
    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

# Use computed properties like computed values!
rect = Rectangle(5, 3)
print(rect.area)      # 15 - calculated automatically
print(rect.perimeter) # 16 - calculated automatically
```

Now, let's create a a class with methods that contains the `@property` decorators with the getter, setter and deleter!

```json
class Temperature:
    def __init__(self):
        self._temp = 0 # Protected attribute

    @property
    def temperature(self):
        return self._temp # Getter method that returns the protected attribute

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._temp = value # Setter method that defines a new value into the protected attribute

    @temperature.deleter
    def temperature(self):
        print("Resetting temperature to 0")
        self._temp = 0 # Use "del" for attribute deletion

#  Wield with all functionalities
temp = Temperature()

# Use the setter with validations
temp.temperature = 25
print(temp.temperature)  # 25

# temp.temperature = -300  # Would raise ValueError

# Use the deleter method
del temp.temperature
print(temp.temperature)  # 0
```

Create a more complex example with a game score

```json
class Player:
    def __init__(self, name):
        self.name = name # Public attribute
        self._score = 0 # Two protected attributes
        self._level = 1

    @property
    def score(self):
        return self._score # Getter method

    @score.setter
    def score(self, value): # Setter method
        if value >= 0:
            self._score = value
            self._level = (value // 1000) + 1 # Commenting bug btw
        else:
            raise ValueError("Score cannot be negative")

    @score.deleter
    def score(self):
        print(f"Resetting {self.name}'s progress")
        self._score = 0
        self._level = 1 # Deleter method (also used for resetting data to its original starting value)

    @property
    def level(self):
        return self._level # Another getter method

# Initialize an instance
player = Player("Alice")
player.score = 2500
print(f"Score: {player.score}, Level: {player.level}")  # Score: 2500, Level: 3

# Delete/reset the stored data in the attributes
del player.score
print(f"Score: {player.score}, Level: {player.level}")  # Score: 0, Level: 1

# All output:
15
16
25
Resetting temperature to 0
0
Score: 2500, Level: 3
Resetting Alice's progress
Score: 0, Level: 1
```

**KEY POINT:** Advanced property decorators allow computed properties (calculated from other data), property deletion with `@property.deleter` and full control over getting, setting and deleting attributes. This creates intuitive interfaces while maintaining **strong data validation and encapsulation**.

More examples in practice.py lines 629 - 675.

## Special Methods/Dunder Methods:

### Magic/Dunder Methods Introduction:

Magic methods (also called dunder methods) are special methods with double underscores from both sides, Python calls them automatically in response to certain operations. Here is an example of a class with a magic method:

```json
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"
```

The `__init__` method is called automatically when initializing instances and the `__str__` method is called when you convert the object into a string:

```json
my_book = Book("Python Programming", "John Smith", 350) # Creating an instance

print(my_book)        # Calls __str__ automatically
print(str(my_book))   # Also calls __str__

# Output:
Python Programming by John Smith
Python Programming by John Smith
```

**NOTE:** Without `__str__`, printing would show the object's memory location.

```json
class SimpleBook:
    def __init__(self, title):
        self.title = title

simple = SimpleBook("Test Book")
print(simple)  # <__main__.SimpleBook object at 0x...>
```

We can also add another magic method for length!

```json
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

my_book = Book("Python Programming", "John Smith", 350)
print(len(my_book))   # Calls __len__ automatically

# Output:
350
```

**KEY POINT:** Magic/dunder methods **start and end with double underscores (**method**)**, and are called automatically by Python. They allow your objects to work with built-in functions like `str()`, `len()` and operators, making your classes more pythonic and intuitive to use.

More examples in my_class.py lines 454 - 467 and usage in Main.py lines 181 - 186.

### Operator Overloading:

Operator overloading allows your classes to work with Python's built-in operators (+, -, \*, /, etc) by implementing special dunder methods. Here is an example of a class with operator overloading:

```json
class Vector:
    def __init__(self, x, y): # Constructor dunder method
        self.x = x
        self.y = y

    def __add__(self, other): # Add dunder method
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar): # Multiplication dunder method
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self): # Str dunder method
        return f"Vector({self.x}, {self.y})"

# The __add__ method defines what happens when you use the '+' operator
v1 = Vector(2, 3)
v2 = Vector(5, 7)
result = v1 + v2  # Calls v1.__add__(v2)
print(result)

# The __mul__ method defines what happens when you use the '*' operator
v3 = Vector(5, 6)
scaled = v3 * 3 # Calls v3.__mul__(3)
print(scaled)

# Output: (The answers will be laid out as a vector)
Vector(7, 10)
Vector(15, 18)
```

We can also add comparison operators!

```json
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other): # Equal (comparison) operator dunder method
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3) # Both v1 and v2 are equal, but not v3
v2 = Vector(2, 3)
v3 = Vector(1, 1)

print(v1 == v2)  # True - calls v1.__eq__(v2)
print(v1 == v3)  # False
```

#### Other Mathematical dunder method operators:

- `__truediv__`: For '/' (true division) where the result will be containing decimal places;
- `__floordiv__`: For '//' (floor division) where the result will be rounded down to a whole integer;
- `__sub__`: For '-' (subtraction).

**KEY POINT:** Operator overloading uses magic methods like `__add__` (+), `__sub__` (-), `__mul__` (\*), `__truediv__` (/), `__floordiv__` (//), `__eq__` (==) to define how operators work with your objects. This makes your classes behave naturally with Python's built-in operators!

Examples in practice.py lines 678 - 705.

### Container Magic Methods:

Container magic methods allow your classes to behave like built-in containers (for examples, lists, sets, dictionaries and etc). They enable indexing, length checking and iteration in your custom objects. Here is an example of a class with container magic methods:

```json
class CustomList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items
```

Let's dive deep into the meaning and purpose of these dunder container methods!

| **Container Method** | **Meaning**                        | **Purpose**                                                                    |
| :------------------: | ---------------------------------- | ------------------------------------------------------------------------------ |
|      `__len__`       | Length of a container              | To retrieve the length of a container (also makes `len()` work).               |
|    `__getitem__`     | Get an iterable/element            | Enables indexing for the retrieval of specific elements in a container.        |
|    `__setitem__`     | Assign a new value                 | Enables indexing for assigning one or a sequence of elements into a container. |
|      `__iter__`      | Iterate through a container        | Allows iteration for a container to retrieve multiple values (using a loop).   |
|    `__contains__`    | Verify the existence of an element | To make the `in` operation work for element checking (membership testing).     |

```json
# Using the __len__ method
my_list = CustomList([1, 2, 3, 4])
print(len(my_list))  # 4

# Using __getitem__
print(my_list[2])    # 3
print(my_list[0])    # 1

# Using __setitem__
my_list[1] = 10
print(my_list[1])    # 10

# Using __iter__
for item in my_list:
    print(item)

# Using __contains__
print(3 in my_list)     # True
print(100 in my_list)   # False

# Output:
4
3
1
10
1
10
3
4
True
False
```

**KEY POINT:** Container magic methods like `__len__()`, `__getitem__()`, `__setitem__()`, `__contains__()` and `__iter__()` make your custom classes behave like built-in containers. This provides intuitive indexing, iteration and membership testing for your objects.

More examples in practice.py in lines 710 - 919.

## Advanced OOP Concepts:

### Composition vs Inheritance:

Object-oriented programming offers two main approaches for code reuse: Inheritance ("is-a" relationship) and Composition ("has-a" relationship). Here is an example of inheritance creating "is-a" relationship:

#### Inheritance: "is-a" relationship

```json
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):  # Dog "is an" Animal
    def bark(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.eat())   # Inherited method
print(dog.bark())  # Own method
```

Now, here is an example of composition creating "has-a" relationship:

#### Composition: "is-a" relationship

```json
class Engine:
    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"

class Car:  # Car "has an" Engine
    def __init__(self):
        self.engine = Engine()  # Composition

    def start(self):
        return self.engine.start()

car = Car()
print(car.start())  # Uses composed engine
```

Let's compare both approaches with a slight more complex example:

```json
# Inheritance approach
class Bird:
    def move(self):
        return "Flying"

class Duck(Bird):
    def quack(self):
        return "Quack!"

# Composition approach
class FlyBehavior:
    def move(self):
        return "Flying"

class SwimBehavior:
    def move(self):
        return "Swimming"

class Duck:
    def __init__(self):                         # The instance is first initialized in the Duck class
        self.fly_behavior = FlyBehavior()       # Then the same instance is then initialized in fly_behavior and swim_behavior
        self.swim_behavior = SwimBehavior()     # The instance was NOT inherited from these composite classes, but they are made up of these parts!

    def fly(self):
        return self.fly_behavior.move()

    def swim(self):
        return self.swim_behavior.move()

    def quack(self):
        return "Quack!"
```

Test both approaches:

```json
# Inheritance
duck1 = Duck()       # The Duck "is-a" Bird!
print(duck1.move())  # Flying
print(duck1.quack()) # Quack!

# Composition
duck2 = Duck()       # The Duck "has-a" fly_behavior and swim_behavior!
print(duck2.fly())   # Flying
print(duck2.swim())  # Swimming
print(duck2.quack()) # Quack!
```

Output:

```json
Buddy is eating
Woof!
Engine started
Flying
Quack!
Flying
Swimming
Quack!
```

#### **KEY DIFFERENCES**:

**INHERITANCE**:

- Tight coupling between parent and child classes;
- "Is-a" relationship;
- Changes to the parent class affect all children classes;
- Best for true hierarchical relationships.

**COMPOSITION**:

- Loose coupling between objects;
- "Has-a" relationship;
- Can be more flexible and change behavior at runtime;
- Easier to test and modify.

##### Summary Table:

|  **Aspect**  | **Inheritance ("is-a")** | **Composition ("has-a")** |
| :----------: | ------------------------ | ------------------------- |
| Relationship | Is-a                     | Has-a                     |
|   Coupling   | Tight                    | Loose                     |
| Flexibility  | Less flexible            | More flexible             |
|  Code reuse  | Via subclassing          | Via combining components  |
|  Hierarchy   | Class hierarchy          | Object assembly           |
|   Examples   | Dog inherits Animal      | Car has Engine            |

**KEY POINTS**:

- Use **inheritance** when classes share a clear hierarchical relationship;
- Use **composition** when you want to build complex objects by combining simpler, reusable components;
- Prefer composition for greater flexibility and maintainability in large or evolving codebases;
- Use inheritance when you have a **true "is-a" relationship (clear logical relationships like Dog is an Animal, Cat is an Animal...)**. Use composition when you need flexibility and loose coupling. The principle "composition over inheritance" suggests favoring composition for most cases due to its flexibility and maintainability.

Examples of usage in practice.py lines 923 - 1118.

### Mixins:

Mixins are a special kind of inheritance used to "mix in" **additional functionality** to classes through **multiple inheritance**. They provide specific methods without being complete classes themselves. Here is an example of a simple mixin:

```json
class JSONSerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class User(JSONSerializableMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email
```

The mixin add JSON functionality to any class that inherits from it.

```json
user = User("Alice", "alice@example.com")
print(user.to_json())
```

Output:

```json
{ "name": "Alice", "email": "alice@example.com" }
```

You can create multiple mixins with distinct functionalities:

```json
class PrintableMixin:
    def pretty_print(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

class ComparableMixin:
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
```

Then combine multiple mixins in one class:

```json
class Product(JSONSerializableMixin, PrintableMixin, ComparableMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price

product1 = Product("Laptop", 999)
product2 = Product("Laptop", 999)
```

Use all mixin functionalities:

```json
print(product1.to_json())        # From JSONSerializableMixin
product1.pretty_print()          # From PrintableMixin
print(product1 == product2)      # From ComparableMixin
```

Output:

```json
{"name": "Laptop", "price": 999}
name: Laptop
price: 999
True
```

#### Purpose of Mixins:

- **Code Reuse:** Share common methods across different classes without duplicating code;
- **Separation of Concerns:** Keep distinct behaviors in separate, focused classes;
  **Enhance Classes:** You can also add specific features like serialization, logging, comparison and etc to any class, regardless of its main hierarchy.

#### Importance & Flexibility:

- **Flexible Composition:** You can combine multiple mixins to add various features toa class as needed;
- **Avoid Deep Hierarchies:** Mixins prevent the need for deep or complex inheritance trees;
- **Plug-and-play:** Easily add or remove functionality by including or excluding mixins in your class definition!

#### Key Characteristics of Mixins:

- They are not meant to be instantiated on their own (by any means!);
- Provide specific, reusable functionality (must be distinct from other mixins);
- Don't usually have the constructor method `__init__`;
- Name of the class would usually end with "Mixin" or "able" (naming conventions);
- Can be combined with multiple inheritance;
- You can combine several multiple mixins in one class for rich, modular behavior;
- **Order Matters:** In multiple inheritance, the order of mixins can affect method resolution (MRO)!

#### Summary Table:

|   **Aspect**   | **Mixins**                             |
| :------------: | -------------------------------------- |
|     Usage      | Add reusable methods co classes.       |
| Instantiation  | Not meant to be instantiated directly. |
|  Flexibility   | Combine multiple mixins as needed.     |
| Responsibility | Each mixin should do one thing well.   |
|  Inheritance   | Used with multiple inheritance.        |

**Key Point:** Mixins provide a way to share functionality across different class hierarchies without creating complex inheritance trees. They allow you to "mix in" specific capabilities like serialization, comparison, or printing to any class that needs them. This promotes code reuse and keeps classes focused on their primary responsibilities.

Examples of mixins in practice.py, lines 1120 - 1316.

### Static and Class Methods:

Besides regular instance methods, classes can have static methods and class methods that serve different purposes. Here is an example of a static method:

#### @staticmethod:

```json
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(number):
        return number % 2 == 0
```

Static methods don't need neither the `self` or the `cls` parameter since they work like regular functions. You can call them directly from the class:

```json
result = MathHelper.add(5, 3)
print(result) # 8

check = MathHelper.is_even(10)
print(check) # True
```

Now, here is an example of a class method:

#### @classmethod:

```json
class Person:
    count = 0  # Class variable / class attribute

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_count(cls): # This takes the "cls" parameter!
        return cls.count

    @classmethod
    def create_anonymous(cls):
        return cls("Anonymous")
```

The class methods can take both instances or classes for accessing the class methods with `cls` as the first parameter.

```json
person1 = Person("Alice")
person2 = Person("Bob")
print(Person.get_count())  # 2
```

Use class methods all alternative constructors!

```json
anonymous = Person.create_anonymous()
print(anonymous.name)      # Anonymous
print(Person.get_count())  # 3
```

Compare **all three method types** in **one class:**

```json
class Calculator:
    brand = "Python Calc" # Class attribute

    def __init__(self, owner):
        self.owner = owner

    # Normal instance method - needs self, accesses instance data
    def show_owner(self):
        return f"Owned by {self.owner}"

    # Class method - needs cls, accesses class data
    @classmethod
    def get_brand(cls):
        return cls.brand

    # Static method - needs neither, just a utility function
    @staticmethod
    def multiply(x, y):
        return x * y

calc = Calculator("Alice")
print(calc.show_owner())        # Owned by Alice
print(Calculator.get_brand())   # Python Calc
print(Calculator.multiply(4, 5)) # 20
```

Overall output:

```json
8
True
2
Anonymous
3
Owned by Alice
Python Calc
20
```

You can call class and static methods with instances too!

```json
calc = Calculator("Bob")
print(calc.get_brand())      # Python Calc (class method)
print(calc.multiply(2, 3))   # 6 (static method)
```

#### **KEY DIFFERENCES:**

- **Instance Methods:** Need `self` to access instance data;
- **Class Methods:** Need `cls` to access class data, also good for alternative constructors;
- **Static Methods:** Need neither, just utility functions related to the class.

**KEY POINT:** Use the decorators `@staticmethod` for **utility functions** that belong logically in the class but won't need class or instance data. Use `@classmethod` when you need **access to the class directly**, like for alternative constructors or accessing class attributes.

More examples in practice.py lines 1319 - 1417.

### Class Decorators:

Class decorators allows you to **modify and enhance class by wrapping them with another defined function(s**) (like nested `def` functions), They work like function decorators but they are applied to entire classes.

#### Simple Class (no decorators):

Here is a simple class with no decorators:

```json
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"
```

#### With a class decorator:

We create a new class decorator that adds a new method:

```json
def add_farewell(cls):
    def farewell(self):
        return f"Goodbye from {self.name}"

    cls.farewell = farewell  # Add the method to the class
    return cls
```

Then apply the decorator to the class using the '@' at-sign:

```json
@add_farewell
class EnhancedPerson:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"
```

Now, the `EnhancedPerson` class has its original method and an added method:

```json
person = EnhancedPerson("Alice")
print(person.greet())     # Hello, my name is Alice
print(person.farewell())  # Goodbye from Alice
```

##### Purpose & Importance:

- **Enhance or modify class behavior** without changing the original class code;
- **Add new methods** or **attributes** to a class dynamically;
- **Implement cross-cutting concerns**, like logging, validation, registration in a reusable way;
- **Promote code reuse and separation of concerns** by keeping enhancements outside the main class definition.

##### Example of a Class Decorator in use:

```json
def add_repr(cls):              # Outer function takes the class as an argument
    def __repr__(self):         # New method to add
        return f"{cls.__name__}({self.__dict__})"
    cls.__repr__ = __repr__     # Attach method to the class
    return cls                  # Return the modified class

@add_repr
class User:
    def __init__(self, name):
        self.name = name

u = User("Alice")
print(repr(u))  # Output: User({'name': 'Alice'})
```

In a class decorator, the outer def function takes the class as its argument, modifies or enhances it (for example, by adding methods or attributes), and then returns the modified class.

##### **Key Characteristics:**

- Applied with `@decorator_name` above the class definition;
- Can add, modify, or wrap class methods and attributes;
- Work at the class level, not the instance level;
- Useful for metaprogramming and dry code.

#### Summary Table:

| **Aspect**  | **Class Decorators**                            |
| :---------: | ----------------------------------------------- |
|    Usage    | To modify or enhance classes dynamically.       |
|   Syntax    | `@decorator_name` above the class definition.   |
| Flexibility | Add methods, attributes, behaviors and etc.     |
| Importance  | For reusability, cleaning, separation of logic. |

**KEY POINT:** Class decorators take a class as input, modify or enhance it, and return the modified class. They can add methods, modify attributes, or wrap existing functionality. Use the `@decorator_name` above the class definition to apply then, this provides a **clean way to extend class functionality without inheritance!**

There is a complex example of class decorators in practice.py between lines 1419 - 1564.

### Context Managers:

Context managers allow you to **allocate and release resources precisely** when needed, they ensure **proper cleanup** even if errors occur. Here is the most common example using the `with` statement:

#### Most Common Use Example:

```json
with open('example.txt', 'w') as file:
    file.write('Hello, world!')
# File is automatically closed here
```

The file is automatically closed after the indented block of code, even if an exception occurs!
We can implement our own context manager using the dunder methods `__enter__` and `__exit__` methods:

#### With the `__enter__` and `__exit__` Magic Methods:

```json
class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self # Return self to allow context variable assignment

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")
        return False  # Don't suppress exceptions (return true if you suppose to!)
```

#### Custom Context Manager:

Then, you could use your custom context manager:

```json
with MyContext() as ctx:
    print("Inside the context")
```

Output:

```json
Entering the context
Inside the context
Exiting the context
```

#### Complex examples with a Database:

Create a more practical context manager for database connections!

```json
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        print(f"Connecting to {self.db_name}")
        self.connection = f"Connection to {self.db_name}"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}")
        self.connection = None

with DatabaseConnection("users_db") as conn:
    print(f"Using {conn}")
    print("Performing database operations...")
```

#### Handling exceptions in Context Managers:

And we will have to handle exceptions in context managers:

```json
class SafeContext:
    def __enter__(self):
        print("Setting up resources")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Cleaning up resources")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return False  # Don't suppress the exception

with SafeContext():
    print("Working with resources")
    # raise ValueError("Something went wrong")  # Uncomment to test
```

Outputs:

```json
Connecting to users_db
Using Connection to users_db
Performing database operations...
Closing connection to users_db
Setting up resources
Working with resources
Cleaning up resources
```

#### The `__enter__` Method:

- Runs at the start of the `with` block and sets up resources.

#### The `__exit__` Method:

Note that the `__exit__` dunder method receives three parameters:

- `exc_type`: Exception type (or `None`);
- `exc_val`: Exception value (or `None`);
- `exc_tb`: Exception traceback (or `None`).

#### Key Characteristics:

- Used with the `with` statement;
- Implement `__enter__` and `__exit__`;
- Can handle exceptions gracefully;
- Promote robust, maintainable code.

##### Importance im OOP:

- **Resource Management:** Ensures files, networks connections, locks, ... are always released;
- **Error Safety:** Cleanup happens even if exceptions occur;
- ** Cleaner Code:** Reduces boilerplate and manual cleanup;
- **Encapsulation:** Bundles setup and teardown logic inside a class.

**KEY POINT:** Context Managers use `__enter__` and `__exit__` methods to **manage resources**, the `with` statement **automatically calls these methods**, ensuring proper setup and cleanup. This is especially used for files, database connections and other resources that need guaranteed cleanup.

Example of a Context Manager to be found in practice.py lines 1567 - 1590.

## Advanced Arguments:

### The `*args`:

The `*args` parameter allows a method to accept any number of positional arguments, where the **asterisk '\*'** collects all extra positional arguments into a tuple. Here is an example of a method using the `*args` parameter:

#### Basic Usage of the `*args` parameter:

```json
class Calculator:
    def add_numbers(self, *args):
        return sum(args)

    def show_numbers(self, *args):
        for i, num in enumerate(args):
            print(f"Number {i+1}: {num}")
```

We can call the methods with different numbers of arguments:

```json
calc = Calculator()
result1 = calc.add_numbers(1, 2, 3)
result2 = calc.add_numbers(10, 20, 30, 40, 50)
print(result1)  # 6
print(result2)  # 150
```

The `*args` collects all arguments into a tuple:

```json
calc.show_numbers(5, 10, 15, 20)
```

Output:

```json
6
150
Number 1: 5
Number 2: 10
Number 3: 15
Number 4: 20
```

Note that the `*args` parameter can have any naming convention of your choice, but always remember of the asterisk at the beginning...

#### Combining Regular Parameters:

You can combine regular parameters with the `*args`:

```json
class Logger:
    def log_message(self, level, *messages):
        print(f"[{level}]", end=" ")
        for message in messages:
            print(message, end=" ")
        print()  # New line

logger = Logger()
logger.log_message("INFO", "User", "logged", "in")
logger.log_message("ERROR", "Connection", "failed")
```

Output:

```json
[INFO] User logged in
[ERROR] Connection failed
```

#### Applying the `*args` in Constructor Methods:

```json
class Team:
    def __init__(self, team_name, *players):
        self.team_name = team_name
        self.players = list(players)

    def show_team(self):
        print(f"Team: {self.team_name}")
        for player in self.players:
            print(f"- {player}")

team = Team("Warriors", "Alice", "Bob", "Charlie", "Diana")
team.show_team()
```

Output:

```json
Team: Warriors
- Alice
- Bob
- Charlie
- Diana
```

#### Unpacking Arguments:

You can also unpack arguments when calling methods:

```json
numbers = [1, 2, 3, 4, 5]
result = calc.add_numbers(*numbers)  # Unpacks the list (the numbers have been removed from the list!)
print(result)  # 15
```

**KEY POINT:** The `*args` **collects any number or elements of positional arguments into a tuple**, use this when you don't know how many arguments will be passed to a method. Remember the the name `args` is **conventional and you could use any name after the asterisk**, but `args` is the standard.

Check the example in practice.py in lines 1592 - 1620.

### The `**kwargs`:

`**kwargs` is short for "keyword arguments", it allows a function to accept any element of named arguments (like `key=value` pair) without having to define them in advance.

#### How it Works:

- **`*args`** -> Collects extra positional arguments into a tuple '()'; -**`**kwargs**`** -> Collects extra keyword arguments into a dictionary '{key : value}'.

#### Simple Example:

```json
def greet(**kwargs):
    print(kwargs)

greet(name="Alice", age=25, country="Australia")
```

Output:

```json
{ "name": "Alice", "age": 25, "country": "Australia" }
```

As you can see, the `**kwargs` automatically takes all of the keyword arguments and passes them into a dictionary to be then stored into the `kwargs` variable!

##### Using the Dictionary:

Since the `**kwargs` generates a clean dictionary, you can most certainly loop through it, depending on what iterables you would like to obtain from:

```json
def print_info(**kwargs):
    print("Information received:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Bob", age=30, job="Teacher")
```

Output:

```json
Information received:
name: Bob
age: 30
job: Teacher
```

##### Mixing regular arguments with `**kwargs`:

You can also combine regular parameters with the `**kwargs` just like the `*args` parameter!

```json
def create_profile(name, **details): # The kwargs parameter can also have different naming conventions!
    print(f"Creating profile for: {name}")
    print("Additional details:")
    for key, value in details.items():
        print(f"  {key}: {value}")

create_profile("Sarah", age=28, city="London", hobby="Reading")
```

Output:

```json
Creating profile for: Sarah
Additional details:
  age: 28
  city: London
  hobby: Reading
```

##### Empty `**kwargs`:

If no **keyword arguments are passed**, the `kwargs` parameter will be instantiated as an **empty dictionary**. For example:

```json
def show_data(**kwargs):
    if kwargs:
        print("Data:", kwargs)
    else:
        print("No data provided")

show_data()  # No arguments
show_data(item="apple")  # With arguments
```

Output:

```json
No data provided
Data: {'item': 'apple'}
```

#### Real-World example with `**kwargs`:

Here, you will see why you would use the `**kwargs` parameter in a class:

```json
class Person:
    def __init__(self, name, **kwargs):
        self.name = name
        self.details = kwargs

    def show_info(self):
        print(f"Name: {self.name}")
        for key, value in self.details.items():
            print(f"{key}: {value}")

person = Person("Alice", age=25, city="New York", job="Engineer")
person.show_info()
```

Output:

```json
Name: Alice
age: 25
city: New York
job: Engineer
```

#### Unpacking Dictionaries:

You can also unpack dictionaries when calling functions!

```json
def display_settings(**kwargs):
    for setting, value in kwargs.items():
        print(f"{setting} = {value}")

settings = {"debug": True, "verbose": False, "timeout": 30}
display_settings(**settings)  # Unpacks the dictionary (removes all key-value pairs inside the dictionary)
```

Output:

```json
debug = True
verbose = False
timeout = 30
```

#### **KEY POINTS**:

- The `**kwargs` collects keyword arguments into a dictionary;
- The name `kwargs` is **conventional**, and can be swapped with any other name;
- Use this for flexible function signatures;
- Great for handling optional parameters or configuration settings.

Example in practice.py lines 1622 - 1634.

## Design Patterns Part 1:

### Introduction to Design Patterns:

Design Patterns are reusable solutions to common problems in software design, they are like blueprints that you can customize to solve recurring design problems in your code. Think of design patterns as proven templates that experienced developers use to solve similar problems. When you say, "I used the Singleton pattern," other developers immediately understand the structure of your code. Here is a simple example of why patterns matter:

#### Without Design Patterns:

```json
# Without pattern - messy approach
class DatabaseConnection:
    def __init__(self):
        self.connection = "Connected to database"

# Problem: Multiple connections created
db1 = DatabaseConnection()
db2 = DatabaseConnection()  # Wasteful - creates another connection
```

#### With Design Patterns:

With a design pattern, you get a better solution!

```json
# With Singleton pattern - controlled approach
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Connected to database"
        return cls._instance

# Now only one connection exists
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True - same instance
```

##### Explanation of the code above:

- `DatabaseConnection._instance` is a class variable (a protected class attribute) that stores the single instance;
- The `__new__` dunder method checks if `_instance` is set to `None` (signifies that no instances have been initialized or created yet);
- If so, it creates a new instance and sets up the connection;
- If an instance already exists, it returns the existing one;
- Note that both `db1 is db2` is `True` because they refer to the same object (in terms of memory address!), preventing multiple distinct connections to the database (resource waste). This guarantees a single, shared point of access;

#### The Singleton Design Pattern:

The code above relates to the "Singleton design pattern", and note that this pattern:

- Ensures that **only one instance** of a class exists throughout the program;
- This is very useful for managing shared resources (e.g. database connections, configuration managers...).

##### Why use Design Patterns?

- **Reusability:** For solutions that can be reapplied to similar problems;
- **Communication:** Common vocabulary among developers;
- **Best Practices:** Time-tested solutions;
- **Maintainability:** Well-structured and organized code.

#### What will be mentioned in Design Patterns:

##### **Creational Patterns:**

How these objects will be constructed:

- Singleton Pattern - One instance only;
- Factory Pattern - Create objects without specifying the exact class.

##### **Structural Patterns:**

How objects are composed:

- Adapter Pattern - Make incompatible interfaces work together;
- Decorator Pattern - Add functionality without changing the structure.

##### **Behavior Pattern**:

How objects interact:

- Observer pattern - Notify multiple objects of changes;
- Strategy Pattern - Switch algorithms dynamically;
- Command Pattern - Encapsulate requests as objects.

#### Roles of the distinct patters:

Each pattern have their pros and cons, so it is key to note that each pattern will:

- Be able to solve specific problems;
- Have different ways to implement them into Python;
- Specific times to use it;
- Contain real-world examples.

**KEY POINT:** Design patterns are proven solutions to programming problems, they provide a shared vocabulary and best practices that make your code more maintainable, flexible and easier to understand. We will go through 7 essential patterns that every Python developer should know.

### Singleton Pattern:

The **Singleton Pattern** ensures that a **class has only one instance and it provides a global point of access to it**. This is useful for resources like database connections or configuration settings. Here is the simple singleton pattern which you already have seen in the introduction of this topic:

```json
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

The `__new__` dunder method controls new object creations, where is has a specific role of verifying if an instance has already been instantiated before creating a new one.

Here we create two instances of the Singleton class:

```json
singleton1 = Singleton()
singleton2 = Singleton()
```

Then check of both variables reference the same object:

```json
print(singleton1 is singleton2)  # True
print(id(singleton1))            # Same memory address
print(id(singleton2))            # Same memory address
```

#### Practical Example:

Let's see a more practical example of a Singleton pattern which involves a database connection:

```json
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Connected to MySQL database"
            print("Creating new database connection")
        return cls._instance

    def query(self, sql):
        return f"Executing: {sql}"

# First access creates the connection
db1 = DatabaseConnection()
print(db1.connection)

# Second access reuses the same connection
db2 = DatabaseConnection()
print(db2.connection)

print(db1.query("SELECT * FROM users"))
print(db1 is db2)
```

Next, create a configuration manager using the Singleton Design:

```json
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {} # Instance attribute
        return cls._instance # Return the protected instance

    def set_setting(self, key, value):
        self.settings[key] = value

    def get_setting(self, key):
        return self.settings.get(key)

config1 = Config()
config1.set_setting("debug", True)

config2 = Config()
print(config2.get_setting("debug"))  # True - same settings
```

Output:

```json
True
140234567890123
140234567890123
Creating new database connection
Connected to MySQL database
Connected to MySQL database
Executing: SELECT * FROM users
True
True
```

#### Summary:

**KEY POINT:** The Singleton Pattern utilizes the `__new__()` dunder method to **control object creation, ensuring only one instance exists in the codebase**. Use it for resources that should only have one copy throughout your application, like database connections, loggers or configuration managers. Remember that all variables pointing to a Singleton **references the exact same and original object in a memory address!**

More examples in practice.py lines 1637 - 1740.

### Factory Pattern:

The factory pattern **creates objects without specifying their exact class**. Instead of calling constructors directly, you would use the factory method which will **decide the origin of the object's instantiation**. (decides which class to instantiate from).
Pay close attention to the code below!

#### Example of a Factory Pattern:

```json
class Car: # Both of these classes are vehicles but are distinct from each other (depending on the vehicle type)
    def __init__(self, brand): # __init__ and info methods for both classes
        self.brand = brand
        self.type = "Car"

    def info(self):
        return f"{self.type}: {self.brand}"

class Bike:
    def __init__(self, brand):
        self.brand = brand
        self.type = "Bike"

    def info(self):
        return f"{self.type}: {self.brand}"
```

We create a factory class to produce these objects more precisely:

```json
class VehicleFactory:
    def create_vehicle(self, vehicle_type, brand):
        if vehicle_type == "car":
            return Car(brand) # Composes a Car object
        elif vehicle_type == "bike":
            return Bike(brand) # Composes a Bike object
        else:
            raise ValueError(f"Unknown type: {vehicle_type}")
```

Then utilize the factory class instead of calling constructors directly:

```json
factory = VehicleFactory()
my_car = factory.create_vehicle("car", "Toyota")
my_bike = factory.create_vehicle("bike", "Honda")

print(my_car.info())   # Car: Toyota
print(my_bike.info())  # Bike: Honda
```

#### Using the `*args` parameter:

You can use the `*args` parameter to make your factory class more flexible:

```json
class FlexibleFactory:
    def create_vehicle(self, vehicle_type, *args):
        if vehicle_type == "car":
            return Car(args[0])  # Just brand
        elif vehicle_type == "truck":
            return Truck(args[0], args[1])  # Brand and capacity
        else:
            raise ValueError(f"Unknown type: {vehicle_type}")

class Truck:
    def __init__(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity
        self.type = "Truck"

    def info(self):
        return f"{self.type}: {self.brand} ({self.capacity}t)"
```

Finally, use the flexible factory:

```json
flexible = FlexibleFactory()
car = flexible.create_vehicle("car", "Ford")
truck = flexible.create_vehicle("truck", "Volvo", "20")

print(car.info())    # Car: Ford
print(truck.info())  # Truck: Volvo (20t)
```

Output:

```json
Car: Toyota
Bike: Honda
Car: Ford
Truck: Volvo (20t)
```

#### Key Characteristics:

- The factory pattern operates with **composition** when constructing and instantiating instances with a **factory class**;
- The factory itself is **not a parent class** of the objects it creates;
- Instead, it contains logic to decide which class to instantiate and returns an instance of that specified class;
- The created object is **composed** (assembled) by the factory, not inherited from it;
- This creates flexibility and decouples object creation from the client code.

**KEY POINT:** The factory pattern lets you create objects without knowing their exact class, where the factory class decides where to instantiate based on parameters. Use `*args` to handle multiple products with different constructor parameters, making your code more flexible and easier to extend with new product types!

### Observer Pattern:

The observer pattern creates a **one-to-may relationship** where one **object (subject) notifies multiple objects (observers) when its state changes**. Here is a simple subject class that manages observers:

#### Simple Example:

```json
class Subject: # Represents the subject class
    def __init__(self):
        self._observers = [] # Protected attribute

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)
```

The subject keeps the list of observers and can notify all of them at once. Create simple observer classes:

```json
class EmailNotifier:
    def update(self, message):
        print(f"Email sent: {message}")

class SMSNotifier:
    def update(self, message):
        print(f"SMS sent: {message}")
```

Note that each observer has an `update()` method that gets called when notified!
Now we use the observer pattern:

```json
# Create subject
news = Subject()

# Create observers
email = EmailNotifier()
sms = SMSNotifier()

# Add observers to subject (inserted into the '_observer' protected attribute)
news.add_observer(email)
news.add_observer(sms)

# Notify all observers
news.notify("Breaking news: Python is awesome!")
```

#### Practical Example:

We create a practical example with a stock price tracker:

```json
class Stock: # Represents the subject class
    def __init__(self, symbol, price):
        self.symbol = symbol
        self._price = price
        self._observers = [] # Here, we will store our observers (other instances)

    def add_observer(self, observer):
        self._observers.append(observer) # Method for adding observers

    def set_price(self, price):
        self._price = price
        self.notify()

    def notify(self):
        for observer in self._observers:
            observer.update(self.symbol, self._price) # Iterate through all observers to return the notification!

class Investor:
    def __init__(self, name):
        self.name = name

    def update(self, symbol, price): # This method will be called when the price has been altered
        print(f"{self.name} notified: {symbol} is now ${price}")

# Use the stock tracker
apple_stock = Stock("AAPL", 150)

investor1 = Investor("Alice")
investor2 = Investor("Bob")

apple_stock.add_observer(investor1)
apple_stock.add_observer(investor2)

apple_stock.set_price(155)  # Notifies all investors
```

Output:

```json
Email sent: Breaking news: Python is awesome!
SMS sent: Breaking news: Python is awesome!
Alice notified: AAPL is now $155
Bob notified: AAPL is now $155
```

##### Why use the Observer Pattern?

- **Decouples** the subject from its observers, making code more modular and flexible;
- Allows multiple objects to react to changes in another object \*\*without tight coupling;
- Useful for implementing **event-driven systems**.

##### Other Real-World Uses:

- **GUI Frameworks:** Buttons notify listeners when clicked;
- **Messaging System:** Subscribers get updates when new messages arrive;
- **Logging:** Multiple loggers receive events from an application.

#### Summary:

The observer pattern lets you build systems where objects automatically react to changes in other objects, making your code more modular, flexible and event-driven.

**KEY POINT:** The subject maintains a list of observers and calls their `update()` method when needed. This is useful for notifications, event systems, and keeping multiple parts of your application synchronized.

More examples of usage in practice.py between lines 1933 - 1995.

### Strategy Pattern:

The strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. You can change algorithms at runtime without changing the client code.

#### Simple Example:

Here are simple strategy classes for different payment methods:

```json
class CreditCard: # Strategy classes with their own distinct algorithms
    def pay(self, amount):
        return f"Paid ${amount} with Credit Card"

class PayPal:
    def pay(self, amount):
        return f"Paid ${amount} with PayPal"

class Bitcoin:
    def pay(self, amount):
        return f"Paid ${amount} with Bitcoin"
```

Note that each strategy class implements their own `pay()` method, but with different behaviors. Let's create a context class that uses strategies:

```json
class ShoppingCart: # Context class for utilizing strategy classes/instances
    def __init__(self):
        self.total = 0
        self.payment_strategy = None

    def add_item(self, price):
        self.total += price

    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy

    def checkout(self):
        return self.payment_strategy.pay(self.total)
```

The Context class can switch from different payment strategies, now we use the strategy pattern:

```json
# Create the context instance for strategy manipulation
cart = ShoppingCart()
cart.add_item(50)
cart.add_item(30)

# Use credit card strategy
cart.set_payment_strategy(CreditCard())
print(cart.checkout())

# Switch to PayPal strategy
cart.set_payment_strategy(PayPal())
print(cart.checkout())
```

Output:

```json
Paid $80 with Credit Card
Paid $80 with PayPal
```

#### Sorting Strategies:

Here, we create a sorting strategy:

```json
# Two strategy classes
class BubbleSort:
    def sort(self, data):
        return f"Bubble sorted: {sorted(data)}"

class QuickSort:
    def sort(self, data):
        return f"Quick sorted: {sorted(data)}"

# One context class
class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy # Defines which strategy class to use

    def sort_data(self, data):
        return self.strategy.sort(data) # Calls the sort() method within one chosen strategy

# Use different sorting strategies
numbers = [3, 1, 4, 1, 5]

sorter = Sorter(BubbleSort())
print(sorter.sort_data(numbers))

sorter.set_strategy(QuickSort())
print(sorter.sort_data(numbers))
```

Output:

```json
Bubble sorted: [1, 1, 3, 4, 5]
Quick sorted: [1, 1, 3, 4, 5]
```

##### Why Use the Strategy Pattern?

- **Flexibility:** You can easily swap algorithms or behaviors without modifying the context class;
- **Separation of Concerns:** Keeps algorithms independent from the context, making code cleaner and easier to maintain;
- **Open/Closed Principle:** Add new strategies without changing existing code;
- **Testing:** Each strategy can be tested independently.

#### Other Real-World Uses:

- Payment methods/processes;
- Sorting algorithms;
- Authentication methods (switching between password, OAuth, or biometric authentication strategies).

#### Summary:

The main importance of Strategy Patterns also include:

- Decoupling algorithms from the context;
- Promotion of code re usage and extensibility;
- Makes it easier to add, remove or change behaviors;
- Improves maintainability and testability.

##### Summary Table:

|   **Aspect**   | **Strategy Pattern**                            |
| :------------: | ----------------------------------------------- |
|    Purpose     | Swap algorithms/behaviors at runtime.           |
|   Structure    | Context + interchangeable strategy classes.     |
|    Benefits    | Flexibility, maintainability and extensibility. |
| Real-world use | Payments, sorting, authentications, etc...      |

**KEY POINT:** The strategy pattern lets you swap algorithms at runtime, define different strategies with the same interface, then let the context class choose which one to use. This makes your code more flexible and easier to extend with new algorithms without having to change the codebase.

More examples in practice.py lines 1998 - 2062.

## Design Patterns Part 2:

### Command Pattern:

The command pattern encapsulates a request as an object, allowing you to queue operations, log requests, and support undo functionality. It separates the objects that calls the operation from the one that performs it.

#### Simple Example:

Here are simple command classes:

```json
# Command Classes
class Command:
    def execute(self):
        pass

# Both of these two commands take the receiver object as an argument during initialization
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()
```

Each command (class) encapsulates a specific operation on a receiver object:
Let's create the receiver that actually performs the work:

```json
# Receiver Class
class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")
```

Then create an evoker that executes commands:

```json
# Evoker Class
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()
```

Finally, use the command pattern:

```json
# 1. Create receiver
light = Light()

# 2. Create commands
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

# 3. Create invoker
remote = RemoteControl()

# 4. Execute different commands
remote.set_command(light_on)
remote.press_button()

remote.set_command(light_off)
remote.press_button()
```

#### Undo Operations:

You can add support for for undo operations:

```json
class UndoableCommand(Command):
    def undo(self):
        pass

class LightOnCommand(UndoableCommand):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

class SmartRemote:
    def __init__(self):
        self.last_command = None

    def execute_command(self, command):
        command.execute()
        self.last_command = command

    def undo(self):
        if self.last_command:
            self.last_command.undo()

smart_remote = SmartRemote()
smart_remote.execute_command(LightOnCommand(light))
smart_remote.undo()  # Turns light off
```

Output:

```json
Light is on
Light is off
Light is on
Light is off
```

#### How does it Work?

This pattern involves three main roles:

##### **Command Classes:**

- Encapsulate all information needed to perform an action;
- Each command implements an `execute()` method (and optionally an `undo()` method);
- Examples: `LightOnCommand`, `LightOffCommand`.

###### Should it inherit from ABC and become an abstract class?

Note that the `Command` class in the command pattern is typically used as a **base class** to define a common interface for all command objects. Here is the breakdown:

**If not Abstract: If it does not implement `ABC` and `@abstractmethod` decorators, it simply acts as a **convenience base class**, providing a shared parent for all command classes, which can help with type checking and organization. However, it does **not enforce\*\* that subclasses must implement such methods like the `execute()` method!

**If abstract:** By using `ABC` and `@abstractmethod`, Python will enforce that all subclasses implement the `execute()` method or the `undo()` method (raises an error when you have forgotten to implement the concrete methods). This approach is safer and more robust, ensuring that all commands follow the required interface.

But, it is **best practice** to make the `Command` class as an abstract base class for clarity and safety:

```json
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
```

##### **Receiver Class:**

- Knows how to perform the actual work;
- COntains the business logic or the real operations;
- Examples: `Light` class with `turn_on()` and `turn_off()` methods.

##### **Invoker Class:**

- Holds the triggers commands;
- Does not know the details of how the command is executed.
- Examples: `RemoteControl` class with `set_command()` and `press_button()`.

#### Importance:

- It **decouples sender and receiver**, where the invoker doesn't need to know how the receiver works;
- **Supports undo/redo:** Commands can implement `undo()` for reversible actions;
- **Flexible and extensible:** Easily add new commands without changing existing code (similar to the strategy pattern);
- **Queuing and logging:** Commands cna be stored and executed later.

#### Real-World Examples:

- GUI Buttons and Menus;
- Remote Controls;
- Task Scheduling and Queuing;
- Macro Recording;
- Transaction System;
- Game Development;
- Home Automation.

#### Summary:

| **Role** | **Responsibility**                           |
| :------: | -------------------------------------------- |
| Command  | Encapsulates an action (`execute`, `undo`).  |
| Receiver | Performs the actual work.                    |
| Invoker  | Triggers commands, holds references to them. |

**KEY POINT:** The command pattern turns requests into objects that can be stored, passed around, and executed later. The invoker doesn't need to know how to perform the operations, it just calls `execute()` on the command object. This enables features like undo/redo, queuing operations and logging commands.

Advanced example im practice.py lines 2064 - 2206.

### Adapter Pattern:

The adapter patterns allow objects with incompatible interfaces to work together, it acts as a bridge by wrapping an existing class with a new interface that clients expect.

#### Simple Example:

Here are two systems with incompatible interfaces:

```python
# Two systems with incompatible interfaces:
class OldPrinter:
    def old_print(self, text):
        return f"OLD: {text}"

class NewPrinter:
    def print(self, text):
        return f"NEW: {text}"
```

Notice how the old printer class uses the `old_print()` method while the new printer class utilizes the `print()` method. Now, we'll create an adapter to help bring back the original functioning of the old printer with the new interface!

```python
# Define an Adapter Class for incompatible interfaces to work together (into the expected interface)
class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer # Wields with composition

    def print(self, text):
        # Adapt old interface to new interface
        return self.old_printer.old_print(text)
```

The adapter class wraps the old printer and provides the expected interface.
All that is left to do is to apply both printers into the same client code:

```python
def print_document(printer, text):
    return printer.print(text)  # Expects print() method

# Use new printer directly
new_printer = NewPrinter()
print(print_document(new_printer, "Hello"))

# Use old printer through adapter
old_printer = OldPrinter()
adapter = PrinterAdapter(old_printer)
print(print_document(adapter, "Hello"))
```

When using the adapter instance, the adapter class uses **composition** to simply call the instance which has been passed into the init method inside the Adapter class, making it flexible and easy to call the `OldPrinter`'s `old_print()` method, while simultaneously providing the expected interface in the client code!

Output:

```
NEW: Hello
OLD: Hello
```

#### Example with Media Players:

Create another example with media players:

```python
class Mp3Player:
    def play_mp3(self, filename):
        return f"Playing MP3: {filename}"

class Mp4Player:
    def play_mp4(self, filename):
        return f"Playing MP4: {filename}"

class MediaAdapter:
    def __init__(self, player, audio_type):
        self.player = player
        self.audio_type = audio_type

    def play(self, filename):
        if self.audio_type == "mp3":
            return self.player.play_mp3(filename)
        elif self.audio_type == "mp4":
            return self.player.play_mp4(filename)

class AudioPlayer:
    def play(self, audio_type, filename):
        if audio_type == "mp3":
            return Mp3Player().play_mp3(filename)
        else:
            adapter = MediaAdapter(Mp4Player(), audio_type)
            return adapter.play(filename)

player = AudioPlayer()
print(player.play("mp3", "song.mp3"))
print(player.play("mp4", "video.mp4"))
```

Output:

```
Playing MP3: song.mp3
Playing MP4: video.mp4
```

#### How does it Work?

The **Adapter pattern** primarily uses these types of classes when in action:

##### **System (Adaptee) Classes:**

- These are existing classes with incompatible interfaces (e.g. `OldPinter`, `Mp3Player`, `Mp4Player`);
- They provide useful functionality but don't match the interface expectations by the client code.

##### **Adapter Class:**

- This class wraps (composes) one or more system/adaptee classes;
- It translates the expected interface into calls to the adapter's methods (e.g. `PrinterAdapter`, `MediaAdapter`);
- The Adapter class is the **key component**, since it uses composition over inheritance to delegate calls to the adaptee(s).

###### Why does it use Composition?

- **Composition** allows the adapter to hold a reference to the object it adapts;
- The adapter **delegates calls** to the wrapped object, translating adapters and results as needed;
- This avoids tight coupling and inheritance issues, making the adapter flexible and easy to extend!

Example:

```python
class OldPrinter:
    def old_print(self, text):
        return f"OLD: {text}"

class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer  # Composition

    def print(self, text):
        return self.old_printer.old_print(text)  # Delegation

# Usage
adapter = PrinterAdapter(OldPrinter())
print(adapter.print("Hello"))  # OLD: Hello
```

##### **Client Code** (Class or no class, **Optional**):

- The client interacts with the adapter using the expected interface (e.g. calls `print()` or `play()`);
- Optionally, you may have a client-facing class that uses the adapter internally (e.g. `AudioPlayer`).

#### Key Characteristics:

- **Interface Conversion:** Adapts one interface to another;
- **Composition:** The adapter holds (wraps) an instance of the class it adapts, rather than inheriting from it;
- **Decoupling:** Keeps client code independent from legacy or third-party code;
- **Single Responsibility:** The adapter only translates between interfaces, not business logic!

#### Real-World Examples:

- **Integrating Legacy Systems:** When wrapping an old printer class `old_print()` so it can be used with new code expecting a `print()` method;
- **Media Players:** Adapting an `Mp3Player` and `Mp4Player` to a common `play()` interface;
- **Database Drivers:** Adapting distinct database API's to a unified interface for querying;
- **Payment Gateways:** Wrapping various payment provider SDK's to a standard `process_payment()` method;
- `GUI Frameworks:\*\* Adapting different widgets from different libraries to a common interface.

#### Summary:

|   **Aspect**    | **Adapter Pattern**                         |
| :-------------: | ------------------------------------------- |
|     Purpose     | Bridge incompatible interfaces.             |
|    Mechanism    | Composition (wraps/adapts another object).  |
|   Key Benefit   | Decouples client from legacy/3rd-party.     |
| Real-World uses | Legacy integration, media, payments, GUI... |

**KEY POINT:** The adapter pattern makes incompatible interfaces work together, by wrapping an existing class with a new interface. The adapter translates calls from the expected interface into the actual interface of the wrapped object, this is useful for integrating legacy code or third-party libraries without modifying existing code.

Complex example in practice.py lines 2210 - 2555.

### Decorator Pattern:

The decorator pattern adds new functionality to objects dynamically without changing their structure. It wraps objects to extend their behavior. Here is a simple coffee example:

#### Simple Example:

```python
class Coffee:
    def cost(self):
        return 5

    def description(self):
        return "Simple coffee"
```

Create decorators that add new features into the `Coffee` class:

```python
# Both of these decorators will pass on the Coffee object for composition during initialization
class MilkDecorator:
    def __init__(self, coffee: object):
        self.coffee = coffee # Creates another object inside the MilkDecorator class to be defined as an instance attribute

    def cost(self):
        return self.coffee.cost() + 2 # Calls directly from the Coffee class, mentioning the return value of 5 (originally from the Coffee class) and increments that value with 2

    def description(self):
        return self.coffee.description() + " + Milk" # String concatenation with the Coffee's description() method

class SugarDecorator:
    def __init__(self, coffee: object):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 1

    def description(self):
        return self.coffee.description() + " + Sugar"
```

Each decorator wraps its own object and adds its own functionality. The `milk_coffee` still has access to the original `cost()` and `description()` methods via delegation. Now we use these decorators to build customized coffee:

```python
# Start with basic coffee
my_coffee = Coffee()
print(f"{my_coffee.description()}: ${my_coffee.cost()}")

# Add milk
my_coffee = MilkDecorator(my_coffee)
print(f"{my_coffee.description()}: ${my_coffee.cost()}")

# Add sugar
my_coffee = SugarDecorator(my_coffee)
print(f"{my_coffee.description()}: ${my_coffee.cost()}")
```

Output:

```
Simple coffee: $5
Simple coffee + Milk: $7
Simple coffee + Milk + Sugar: $8
```

#### Example with Text Formatting:

Here is another example with text formatting:

```python
class Text:
    def __init__(self, content):
        self.content = content

    def render(self):
        return self.content

class BoldDecorator:
    def __init__(self, text: object):
        self.text = text

    def render(self):
        return f"<b>{self.text.render()}</b>"

class ItalicDecorator:
    def __init__(self, text: object):
        self.text = text

    def render(self):
        return f"<i>{self.text.render()}</i>"

# Build formatted text step by step
message = Text("Hello World")
message = BoldDecorator(message)
message = ItalicDecorator(message)

print(message.render())
```

Output:

```
<i><b>Hello World</b></i>
```

> [!NOTE]
> When passing on the primary instance of the program to be assigned into/with the decorator class, the decorator **holds the reference** to the original object without overriding it (it operates with composition). It **delegates calls** to the original object for unchanged behavior, and the decorator will only **add or modify** the specific behavior, while all other functionality remains accessible (if the decorator forwards those calls).

#### Key Characteristics:

- **Dynamic Behavior Extension:** Adds new functionality to objects at runtime, without changing their original code;
- **Uses Composition:** The decorator class wraps the original object and holds a reference to it, delegating unchanged behavior;
- **Same Interface:** Decorators implement the same interface as the object they decorate, so they can be used interchangeable;
- **Stackable:** Meaning that multiple decorators can be layered to combine behaviors flexibly;
- **Open/Closed Principle:** Objects are open for extension (via decorators) but closed for modifications;
- **Avoids Subclass Explosion:** No need to create many subclasses for every feature combination, just compose decorators as needed;
- **Transparent to Client:** The client code interacts with the decorated object as if it were the original.

##### How and Why is it Used?

- **How:**

  - You create a decorator class that takes an object and implements the same interface;
  - The decorator forwards calls to the original object, adding extra behavior before or after.

- **Why:**:
  - To extend or modify object behavior at runtime;
  - To follow the **Open/Closed Principle** (open for extensions, closed for modifications);
  - To avoid subclass explosion (many subclasses for every feature combination).

###### Can it use Inheritance?

Sometimes inheritance is used for interface sharing, but **composition** is preferred for flexibility and dynamic extension.

#### Real-World Examples:

- Coffee Shop Example;
- Text Formatting;
- Logging or Authorization, where you would wrap a service object to add logging or permission checks before calling its methods.

#### Summary:

**KEY POINT:** The Decorator Pattern wraps objects to add new functionality and behavior without changing the original object, reminding that each decorator will store the reference to the wrapped object and adding new functionality. This allows you to combine multiple decorators for flexible feature combinations without creating many subclasses.

Example in practice.py lines 2558 - 2943.

### Template Method Pattern:

The Template Method Pattern defines the skeleton of an algorithm in a base class, letting subclasses override specific steps without changing the algorithm's structure.

#### Simple Example:

Here is a base class with a template method:

```python
class DataProcessor: # Main base class
    def process(self): # Template method
        """Template method defining the algorithm structure"""
        self.read_data()
        self.process_data() # This method will need to be implemented...
        self.save_data()

    def read_data(self):
        print("Reading data...")

    def process_data(self):
        raise NotImplementedError("Subclasses must implement this")

    def save_data(self):
        print("Saving data...")
```

The template method `process()` defines the algorithm steps, while `process_date()` is left for subclasses to implement.
Now we create concrete classes that implements the abstract method:

```python
# Child classes that implement their own versions of the process_data() method (overrides the parent's method)
class CSVProcessor(DataProcessor):
    def process_data(self):
        print("Processing CSV data")

class JSONProcessor(DataProcessor):
    def process_data(self):
        print("Processing JSON data")
```

> [!NOTE]
> Note that each concrete class implements their own distinct code for that required step.

Finally, we use the template method:

```python
csv_processor = CSVProcessor()
csv_processor.process()

print()  # Empty line

json_processor = JSONProcessor()
json_processor.process()
```

Output:

```
Reading data...
Processing CSV data
Saving data...

Reading data...
Processing JSON data
Saving data...
```

#### Example with a Game Template:

Let's create another example with a game template:

```python
class Game:
    def play(self):
        """Template method for playing a game"""
        self.start_game()
        self.play_game()
        self.end_game()

    def start_game(self):
        print("Game started!")

    def play_game(self):
        raise NotImplementedError("Define the game rules")

    def end_game(self):
        print("Game ended!")

class Chess(Game):
    def play_game(self):
        print("Playing chess - thinking strategically...")

class Soccer(Game):
    def play_game(self):
        print("Playing soccer - running and kicking...")

chess = Chess()
chess.play()

print() # Prints an empty line

soccer = Soccer()
soccer.play()
```

Output:

```
Game started!
Playing chess - thinking strategically...
Game ended!

Game started!
Playing soccer - running and kicking...
Game ended!
```

#### Key Characteristics:

- **Algorithm skeleton in base class;**
- **Customizable steps via subclassing;**
- **Promotes code reuse and consistency;**
- \*\*Can use abstract base classes (`abc.ABC`);
- **Enforces a fixed sequence of operation.**

##### How and Why are Template Method Patterns Used?

- **How:**

  - You create a base class with a template method that calls several other method;
  - Implement default behavior for some steps in the base class;
  - Mark steps the must be customized (ofter with the `NotImplementedError` exception or `@abstractmethod` decorator);
  - Subclasses override those steps to provide specific behavior.

  Here is an example of a base report generator class with a template method:

  ```python
  # This is the base class with a template method
  class ReportGenerator:
      def generate(self):
          self.fetch_data()
          self.process_data()
          self.format_report()
          self.save_report()

      def fetch_data(self):
          print("Fetching data...")

      def process_data(self):
          raise NotImplementedError

      def format_report(self):
          print("Formatting report...")

      def save_report(self):
          print("Saving report...")

  class SalesReport(ReportGenerator):
      def process_data(self):
          print("Processing sales data")
  ```

- **Why:**
  - **Code Reuse:** Common algorithm structure is reused, only varying the steps that need customization;
  - **Consistency:** Ensures all subclasses follow the same sequence of operations;
  - **Flexibility:** Subclasses can change only the parts they need, without altering the overall flow;
  - **Encapsulation:** Keeps the algorithm's structure in one place, making maintenance easier;
  - **Enforces a Contract:** Subclasses must implement required steps, especially when using the `abc` module.

###### Can it use the ABC Module?

The answer is crystal clear, you can definitely utilize the `abc` module to make the base class abstract and enforce that subclasses implement required steps!

Down below is an implemented example with the `DataProcessor` being inherited from the `abc` module:

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process(self):
        self.read_data()
        self.process_data()
        self.save_data()

    def read_data(self):
        print("Reading data...")

    @abstractmethod
    def process_data(self):
        pass

    def save_data(self):
        print("Saving data...")
```

#### Real-World Examples:

- Data processing: Reading, processing and saving data (CBS, JSON, XML);
- Games: Defining game flow (start, play, end) with different rules for each game;
- Document generation: Steps for preparing formatting and exporting documents;
- Web frameworks: Request handling pipeline with customizable hooks.

#### Summary:

|   **Aspect**    |       **Template Method Pattern**        |
| :-------------: | :--------------------------------------: |
|    Structure    |   Base class defines algorithm steps.    |
|  Customization  |   Subclasses override specific steps.    |
|   ABC support   |   Yes, for enforcing required method.    |
| Real-world uses | Data processing, games, document export. |
|   Key benefit   |  Consistency, code reuse, flexibility.   |

**KEY POINT:** The Template Method Pattern defines a common algorithm structure in the parent class while letting subclasses customize specific steps. The parent class controls the overall flow, but the subclasses provide the specific implementations for specific methods that need implementation. This ensures consistent structure while allowing flexibility in individual steps.

Example in practice.py in lines 2946 - 2998.

### State Pattern:

The State Pattern allows an object to alter its behavior when its internal state changes, the object appears to change its class based on its current state.

#### Simple Example:

Here is a simple example with state classes for a traffic light:

```python
# Three state classes with similar methods and unique state changes
class RedState:
    def next_state(self, light):
        print("Red -> Green")
        light.state = GreenState()

    def current_color(self):
        return "Red"

class GreenState:
    def next_state(self, light):
        print("Green -> Yellow")
        light.state = YellowState()

    def current_color(self):
        return "Green"

class YellowState:
    def next_state(self, light):
        print("Yellow -> Red")
        light.state = RedState()

    def current_color(self):
        return "Yellow"
```

Each state defines what happens when transitioning to the next state.
Let's create a context class that holds the current state:

```python
# This is the context class, where the object can transition into different states!
class TrafficLight:
    def __init__(self):
        self.state = RedState()  # Start with red (utilizing composition for keeping track of these behaviors) while keeping its reference

    def change(self):
        self.state.next_state(self) # You pass 'self' twice to alter the primary instance into another class

    def get_color(self):
        return self.state.current_color()
```

Note that the `TrafficLight` class delegates to its current state object, now all we have to do is operate with the traffic lights!

```python
light = TrafficLight() # Primary instance
print(f"Current: {light.get_color()}")

light.change()  # Red -> Green (note that )
print(f"Current: {light.get_color()}")

light.change()  # Green -> Yellow
print(f"Current: {light.get_color()}")

light.change()  # Yellow -> Red
print(f"Current: {light.get_color()}")
```

Output:

```
Current: Red
Red -> Green
Current: Green
Green -> Yellow
Current: Yellow
Yellow -> Red
Current: Red
```

#### Example with a Player:

Here is another example with a simple player:

```python
# Two state classes
class PlayingState:
    def play(self, player):
        print("Already playing")

    def stop(self, player):
        print("Stopping music")
        player.state = StoppedState()

class StoppedState:
    def play(self, player):
        print("Starting music")
        player.state = PlayingState()

    def stop(self, player):
        print("Already stopped")

# One Context class
class MusicPlayer:
    def __init__(self):
        self.state = StoppedState()

    def play(self):
        self.state.play(self)

    def stop(self):
        self.state.stop(self)

player = MusicPlayer()
player.play()   # Starting music
player.play()   # Already playing
player.stop()   # Stopping music
player.stop()   # Already stopped
```

Output:

```
Starting music
Already playing
Stopping music
Already stopped
```

#### Key Characteristics:

- **Encapsulates state-specific behavior** in separate classes;
- **Context class** holds reference to the current state object;
- **State transition** are handled by changing the state object in the context;
- **Uses composition:** The context contains (wraps) state objects, not inherits from them;
- **Promotes maintainability:** Easy to add new states or change behavior without modifying the context class.

##### How and Why are State Patterns used?

- **How:**

  - You define **separate state classes** for each possible state, where each implements their own unique behavior;
  - You create a **context class** (e.g. `TrafficLight`, `MusicPlayer`) that holds a reference to the current state object;
  - The context delegates actions to its current state object;
  - When an action triggers a state change, the state object updates the context's state to a new state object (the primary instance).

  ```python
  class RedState:
      def next_state(self, light):
          print("Red -> Green")
          light.state = GreenState()

  class TrafficLight:
      def __init__(self):
          # Holds an instance attribute (reference to the state class)
          self.state = RedState()

      def change(self):
          self.state.next_state(self)

  # Here we manipulate with these methods and changes!
  light: object = TrafficLight() # TrafficLight starts in RedState
  light.change() # Delegates to RedState.next_state() transitioning the context to GreenState
  ```

  > [!NOTE]
  > The instance attribute 'self.state' is a reference to the instance from the 'RedState' class and we pass the primary instance and define a new behavior into the 'light.state = GreenState()' line. Note that the context class will handle with the `self.attribute_name` instance attribute and the State class handles with the `instance.attribute_name` instance attribute. The `attribute_name` must be **identical** to both inside the context and state classes for the behaviors to change!

- **Why:**
  - **Encapsulation:** Each state's behavior is kept in its own class, making code easier to manage and extend;
  - **Flexibility:** You can add new states or change behaviors without modifying the context class;
  - **Eliminates Complex Conditionals:** Instead of many 'if' / 'else' statements inside the context, each state handles its own transitions;
  - **Dynamic Behavior:** The object's behavior changes at runtime depending on its current state.

##### Logic Behind the State Pattern:

- The context object doesn't need to know the details of each state's behavior;
- Each state class knows how to handle its own behavior and when/how to transition to other states;
- The context simply delegates actions to the current state, and the state decides what happens next.

#### Why is `self` Passed Twice?

Note that when calling a state object (e.g. `self.state.next_state(self)`), the first `self` is the context object, and the second `self` is passed to the state so it can update the context's state attribute, this allows the state object to modify the context (e.g. switch to a new state).

#### Real-World Uses:

- **Traffic lights:** Switching between red, yellow and green states;
- **Media players:** Switching between playing, paused and stopped states;
- **Order processing:** Changing order status (pending, shipped or delivered);
- **Authentication:** Switching between logged- in and logged-out states.

#### Summary:

|    **Aspect**    | **State Pattern**                            |
| :--------------: | -------------------------------------------- |
|     Purpose      | Change behavior based on internal states.    |
|    Mechanism     | Composition (context holds state object).    |
| State transition | Swap state objects at runtime.               |
| Real-world uses  | Traffic lights, media players, orders...     |
|   Key benefit    | Flexibility, maintainability, extensibility. |

**KEY POINT:** State pattern encapsulates state-specific behavior in separate classes and lets the context object delegate to the current state. When the state changes, the behavior changes automatically. This eliminates complex if/else statements and makes adding new states easier.

Example in practice.py lines 3001 - 3078.

### Composite Pattern:

The Composite Pattern treats individual objects and groups of objects uniformly, it create tree structures where both single items and collections of items share the same interface.

#### Simple Example:

Here are simple components for a file system:

```python
class File: # File class
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def display(self):
        return f"File: {self.name} ({self.size}KB)"

class Folder: # Folder class
    def __init__(self, name):
        self.name = name        # Name of the folder
        self.children = []      # Stores all files within this folder object

    def add(self, item):
        self.children.append(item)

    def get_size(self):
        total = 0
        for child in self.children:
            total += child.get_size()
        return total

    # Method for building the tree structure
    def display(self):  # If the instance stored inside the container is also part of the Folder class, that particular instance will go through this entire line of code as well!
        result = f"Folder: {self.name}"
        for child in self.children:
            result += f"\n  {child.display()}" # Calls the display() method from either, the Folder class or the File class
        return result
```

Both files and folders contain the exact same methods (`get_size()` and `display()`), so they can be treated uniformly.
Build a file system structure:

```python
# Create files
file1 = File("document.txt", 10)
file2 = File("image.jpg", 50)
file3 = File("video.mp4", 200)

# Create folders
documents = Folder("Documents")
media = Folder("Media")
root = Folder("Root")

# Build the tree structure
documents.add(file1)
media.add(file2)
media.add(file3)
root.add(documents)
root.add(media)
```

Then we use the composite structure:

```python
print(f"Root size: {root.get_size()}KB")
print(root.display())
```

Output:

```
Root size: 260KB
Folder: Root
  Folder: Documents
    File: document.txt (10KB)
  Folder: Media
    File: image.jpg (50KB)
    File: video.mp4 (200KB)
```

#### Example with a Menu System:

Create another example with a menu system:

```python
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def show(self):
        return f"{self.name}: ${self.price}"

class Menu:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def get_price(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total

    def show(self):
        result = f"{self.name} Menu:"
        for item in self.items:
            result += f"\n  {item.show()}"
        return result

combo = Menu("Combo")
combo.add(MenuItem("Burger", 8))
combo.add(MenuItem("Fries", 3))
combo.add(MenuItem("Drink", 2))

print(f"Combo price: ${combo.get_price()}")
print(combo.show())
```

Output:

```
Combo price: $13
Combo Menu:
  Burger: $8
  Fries: $3
  Drink: $2
```

#### Key Concepts:

- **Component:** The base interface or abstract class for all objects in the structure (leaf and composite);
- **Leaf:** Represents individual objects (e.g., a file, a menu item) that do not have children;
- **Composite:** Represents groups of objects (e.g. a folder, a menu) that can contain leaves or other composites;
- **Uniformity:** Both leaf and composite objects implement the same interface, so client code can treat them the same way;
- **Recursive Composition:** Composites can contain other composites, enabling deep, nested structures.

##### Structure:

```
        Component
         /      \
      Leaf    Composite
                 |
        children (list of components)
```

#### Key Characteristics:

- **Tree Structure:** Enables hierarchical organization;
- **Uniform Interface:** Treats individual and composite objects the same;
- **Recursive Operations:** Operations like `display()` or `get_size()` are recursive;
- **Extensibility:** Easy to add now types of components;
- **Loose Coupling:** Client code does not need to distinguish between leaf and composite.

#### Real-World Examples:

- **File Systems:** Folders contain files and other folders;
- **Menu:** Menus contain menu items and submenus;
- **Organization Charts:** Managers (composites) and employees (leaves);
- **Graphics Editors:** Groups of shapes and individual shapes.

#### Summary:

| **Concept** | **Description** |
| Component | Base interface for all objects. |
| Leaf | Individual object, no children. |
| Composite | Group of objects can contain leaves/composites. |
| Uniformity | Same interface for all objects. |
| Recursion | Composites operate recursively on children. |

**KEY POINT:** The composite pattern lets you treat individual objects and collection of objects the same way, both leaves (individual items) and composites (groups) implement the same interface. This makes it easier to work with tree structures like file systems, menus or organizational charts.

Complex example in practice.py lines 3081 - 3662.
