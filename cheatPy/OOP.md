## OOP - Object-Oriented Programming

### What is OOP?

OOP or object-oriented programming, is a programming paradigm that uses objects to organise and structure code. This approach helps to make programs easier to understand, maintain and extend.

### What do we use OOP for?

- ***Software development:*** OOP makes it easier to design and implement complex software systems.
Object-oriented programming allows code to be reused in different projects through inheritance and composition.
- ***Modularity:*** OOP promotes modularity, allowing developers to develop separate modules or objects that can be easily integrated into other projects.

### What should we not use OOP for?
- ***Simple scripts or programs:*** if the task is simple and does not require complex data structures or behaviours, OOP may be too complex.
- ***Performance-critical systems:*** In some cases where performance is the most important consideration (e.g. time-critical systems), the overhead of OOP may be a disadvantage.

### What is a class?
A class is a template that defines the state (data members, properties) and behaviour (methods) of an object.

### What are object and methods?
- ***Object:*** an instance of a class. It contains the data and behaviours defined by that class.
- ***Methods:*** Functions that define the behaviour of an object and that access and modify the state (data members) of the object.

```
class Dog:
    def __init__(self, name, age):
        self.name = name  # Property to store the dog's name
        self.age = age    # Property to store the dog's age

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

# Creating objects of the Dog class
dog1 = Dog("Buddy", 4)
dog2 = Dog("Lucy", 2)

# Calling methods on our objects
dog1.bark()  # Buddy says woof!
dog2.bark()  # Lucy says woof!

# Celebrating a birthday for Lucy
dog2.birthday()  # Lucy is now 3 years old.
```

The keyword `self` refers to the current instance (object). When a method is called on an object, Python automatically passes the object as the first parameter to the method. This parameter is called 'self' to indicate that it refers to the current instance of the class.

The purpose of using `self` is to allow the object's attributes and other methods to be referenced within the class.

The `__init__` method serves as the class constructor, which is automatically called when a new object is instantiated from the class. The purpose of the `__init__` method is to initialize the object, i.e., to set up the attributes and the initial state that the object requires at the moment of its creation.

### What is the difference between methods and functions?

- ***Methods:*** Class-bound functions that can only be accessed through a specific object or class, and usually have access to the object's data members.

- ***Functions:*** Independent functions that can perform operations on any type of data and are not tightly bound to a specific object or class.

```
class Dog:
    def __init__(self, name, age):
        self.name = name  # Property to store the dog's name
        self.age = age    # Property to store the dog's age

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

# This is a function, not a method of the Dog class.
def describe_dog(dog):
    print(f"This dog's name is {dog.name} and it is {dog.age} years old.")

# Creating objects of the Dog class
dog1 = Dog("Buddy", 4)
dog2 = Dog("Lucy", 2)

# Calling methods on our objects
dog1.bark()  # Buddy says woof!
dog2.bark()  # Lucy says woof!

# Celebrating a birthday for Lucy
dog2.birthday()  # Lucy is now 3 years old.

# Using the standalone function
describe_dog(dog1)  # This dog's name is Buddy and it is 4 years old.
describe_dog(dog2)  # This dog's name is Lucy and it is 3 years old.
```

### What is class variable?

A class variable in Python is a variable that is shared among all instances of a class. 
Class variables are defined within the class construction but outside any of the instance methods. 
Class variables are not unique to each instance; rather, they are shared across all instances of the class, 
meaning that if you change the value of a class variable for one instance, it changes for all instances.

```
class Dog:
    species = "Canis familiaris"  # Class variable shared by all instances

    def __init__(self, name, age):
        self.name = name  # Instance variable unique to each instance
        self.age = age    # Instance variable unique to each instance

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

    @classmethod
    def get_species(cls):
        return cls.species  # Access the class variable

# Example usage
dog1 = Dog("Buddy", 5)
dog2 = Dog("Lucy", 3)

print(Dog.get_species())  # Accessing class variable through a class method
print(dog1.species)  # Accessing class variable directly from an instance
```

### What is `__dict__ `?

`__dict__` is a special attribute in Python, available in most objects. 
It contains a dictionary that maps attribute names to their values. 

This feature is highly useful for several reasons:

- ***Inspecting Object State:*** It allows for the inspection of an object's state at any point in time, showing all the attributes currently bound to the object and their values.
- ***Dynamic Attribute Management:*** Python's dynamic nature is showcased through the ability to add, modify, or remove attributes from objects at runtime, which can be directly observed through changes in the `__dict__` attribute.
- ***Debugging:*** It can be particularly useful for debugging purposes, as it gives a clear view of what data an object is holding at any given moment.

```
class Dog:
    species = "Canis familiaris"  # Class variable shared by all instances

    def __init__(self, name, age):
        self.name = name  # Instance variable unique to each instance
        self.age = age    # Instance variable unique to each instance

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

# Creating an instance of Dog
my_dog = Dog("Rex", 4)

# Printing the __dict__ attribute of the instance
print(my_dog.__dict__)

# Printing the __dict__ attribute of the Dog class itself
print(Dog.__dict__)
```

### What are `@property` and `@property_name.setter`?

The `@property` decorator in Python is a built-in decorator that allows you to turn class methods into properties. 
This means that you can access method calls as attributes, without the need to use parentheses `()` to call the method. It's particularly useful for defining attributes that are derived from other attributes, or for adding logic to the getting and setting of an attribute's value.

To extend the functionality and make a property writable, you can define a setter for it using the `@property_name.setter` decorator.

```
class Dog:
    def __init__(self, name, age):
        self.name = name  # Property to store the dog's name
        self._age = age    # Private property to store the dog's age

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

    @property
    def age(self):
        """Get the dog's age."""
        return self._age

    @age.setter
    def age(self, value):
        """Set the dog's age with some validation."""
        if value < 0:
            raise ValueError("Age cannot be negative")
        else:
            self._age = value

# Example usage:            
my_dog = Dog("Rex", 5)
my_dog.age = 7
print(my_dog.age)
my_dog.age = -5
print(my_dog.age)
```

### What is `@staticmethod`?

The `@staticmethod` decorator in Python is used to define a method within a class that does not access or modify the class state or instance state. This means that a static method does not take the self parameter, which represents the instance of the `class`, nor does it take a `cls` parameter, which represents the class itself. Static methods behave like regular functions but are included in the class's body to have a logical connection with the class.

```
class Dog:
    def __init__(self, name, age):
        self.name = name  # Property to store the dog's name
        self.age = age    # Property to store the dog's age

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

    @staticmethod
    def general_advice():
        print("Dogs need plenty of exercise and mental stimulation.")

# Example usage:
Dog.general_advice()
```

### What is class Methods?

Methods with the `@classmethod` decorator are used as methods defined at the class level that access the state of the class, but not the state of a particular instance. The `@classmethods` are given the class itself as their first parameter (conventionally called cls), which allows them to access the attributes of the class and other class methods. 

- ***Alternative Constructors***: The most common use is to create alternative constructors. Since the `__init__` method only allows one type of initialization, `@classmethods` can be used to define different initialization logic. For example, if you want to create an instance of a class from multiple sources (e.g., a text file, a database, or a data structure), you can define a separate class method for each source type.

- ***Static Methods vs. Class Methods***: Although methods with the `@staticmethod` decorator work similarly in the sense that they do not access the state of a particular instance, class methods have the advantage of accessing and modifying the state of the class. This allows class-level data to be managed and modified through instances of the class.

- ***Class-level logic***: `@classmethods` can be used to implement class-level logic that is not tightly bound to any single instance. For example, if a class handles the number of instances created or other class-level data, a class method is a great way to handle it.

- ***Inheritance Support***: Class methods can also be useful in inheritance hierarchies, as they allow descendant classes to have their own implementations without overriding the methods of the original class. This is a form of polymorphism that provides greater flexibility in interactions between classes.

```
class Dog:
    def __init__(self, name, age):
        self.name = name  # Property to store the dog's name
        self.age = age    # Property to store the dog's age

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")
    
    @classmethod
    def from_string(cls, data_str):
        """
        Class method to create a Dog instance from a string.
        The string format should be 'name,age'
        """
        name, age = data_str.split(',')
        return cls(name, int(age))

# Example usage:
dog_info = "Rex,5"
rex = Dog.from_string(dog_info)
rex.bark()  # Rex says woof!
rex.birthday()  # Rex is now 6 years old.
```

`@classmethod` is useful when you need to work with class state or alternative constructs within the class, while `@staticmethod` is ideal for functionality that is related to the class but does not depend on the state of the class or instances.

### Inheritance

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (the child or subclass) to inherit attributes and methods from another class (the parent or superclass). This mechanism supports the reuse of existing code and the implementation of polymorphism.

```
class Dog:
    def __init__(self, name, age):
        self.name = name  # Property to store the dog's name
        self.age = age    # Property to store the dog's age

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

# SuperDog class that inherits from the Dog class
class SuperDog(Dog):
    def fly(self):
        print(f"{self.name} is flying!")

    def speak(self):
        print(f"{self.name} says: I can talk!")

# Instantiate and use methods of the SuperDog class
superdog = SuperDog("Krypto", 3)
superdog.bark()        # Calls the bark method from the Dog class
superdog.birthday()    # Calls the birthday method from the Dog class
superdog.fly()         # New method unique to the SuperDog class
superdog.speak()       # New method unique to the SuperDog class
```

### Multilevel inheritance

Multiple inheritance is a powerful feature in Python that allows a class to inherit from more than one parent class. This means a child class can inherit attributes and methods from multiple parent classes, enabling it to combine functionalities or behaviors from those parents. 

```
class Dog:
    def __init__(self, name, age):
        self.name = name  # Property to store the dog's name
        self.age = age    # Property to store the dog's age

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

class SuperDog(Dog):
    def fly(self):
        print(f"{self.name} is flying!")

    def speak(self):
        print(f"{self.name} says: I can talk!")

# LegendaryDog class that inherits from SuperDog
class LegendaryDog(SuperDog):
    def teleport(self):
        print(f"{self.name} has teleported to another location!")

    def timeTravel(self):
        print(f"{self.name} has traveled through time!")

# Instantiate and use methods of the LegendaryDog class
legendarydog = LegendaryDog("Cerberus", 5000)
legendarydog.bark()         # Calls the bark method from the Dog class
legendarydog.fly()          # Calls the fly method from the SuperDog class
legendarydog.speak()        # Calls the speak method from the SuperDog class
legendarydog.teleport()     # New method unique to the LegendaryDog class
legendarydog.timeTravel()   # New method unique to the LegendaryDog class
```

### What is Abstract Base Class (ABC)?

In Python, the Abstract Base Class (ABC) mechanism provides a way to define abstract methods in a class, which must then be implemented by any subclass. 

**Why Use ABCs?**

***Methods to Be Defined:*** ABCs allow you to specify methods that must be implemented by subclasses, thereby ensuring adherence to a defined interface.
***Type Checking:*** With ABCs, you can perform type checking to verify whether an object implements the methods defined in an abstract class.
***Facilitating Code Reuse:*** Abstract classes enable you to define common logic that can then be implemented in various ways by subclasses.

```
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name  # Property to store the animal's name
        self.age = age    # Property to store the animal's age

    @abstractmethod
    def bark(self):
        pass

    @abstractmethod
    def birthday(self):
        pass

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

# Assuming the Animal (ABC) and Dog classes are defined as previously shown

# Create an instance of Dog
my_dog = Dog(name="Buddy", age=5)

# Call the bark method
my_dog.bark()  # Output: Buddy says woof!

# Celebrate the dog's birthday and check its age
my_dog.birthday()  # Output: Buddy is now 6 years old.

# Since Animal is an abstract base class, trying to instantiate it directly would raise an error
# my_animal = Animal(name="Generic Animal", age=10)  # This would raise a TypeError
```

### What is Encapsulation?

Encapsulation allows the data members (properties and methods) of a class to be hidden from external access, so that only methods within the class can modify them. This ensures data integrity and security. Encapsulation can be used to control access to data, for example by using public, private and protected modifiers to determine which classes can access this data.

**Naming conventions**

In Python, naming conventions for variables and methods play an important role in controlling the visibility and accessibility of data members. 

One Underscore (_)
Use the _ (one underscore) prefix to mark data members or methods as "protected" or for internal use. This is a convention among Python programmers and does not prevent access to data members, it merely indicates that they are not intended for direct access from outside. 

Two Underscores (__)
The use of the __ (two underscores) prefix is used to hide data members or methods. This activates the so-called "name mangling" mechanism in Python, which makes it difficult to access data members directly from outside the class.

**Dog Class with Private Attributes**

```
class Dog:
    def __init__(self, name, age):
        self.__name = name  # Private property to store the dog's name
        self.__age = age    # Private property to store the dog's age

    def bark(self):
        print(f"{self.__name} says woof!")

    def birthday(self):
        self.__age += 1
        print(f"{self.__name} is now {self.__age} years old.")

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")

# Creating a Dog object
my_dog = Dog("Buddy", 5)

# Accessing the dog's name and age using getters
print(f"My dog's name is {my_dog.get_name()} and it is {my_dog.get_age()} years old.")

# Making the dog bark
my_dog.bark()

# Celebrating the dog's birthday
my_dog.birthday()

# Trying to change the dog's name and age using setters
my_dog.set_name("Max")
my_dog.set_age(6)

# Accessing the modified name and age
print(f"After an update, my dog's name is {my_dog.get_name()} and it is {my_dog.get_age()} years old.")

# Attempting to set a negative age to demonstrate validation
my_dog.set_age(-1)
```

### Method Overriding

Method Overriding is an object-oriented programming technique that allows you to change the behavior of a method defined in a base class to a method defined in a child class. This means that if you rewrite a method in a descendant class that already exists in the parent class, the rewritten method will run when called on an instance of the descendant class. This may be useful when the generic behavior of the parent class is not appropriate for the specific needs of the descendant class and there is a need to fine-tune the behavior or to specify completely new behavior.

```
class Dog:
    def __init__(self, name, age):
        self.name = name  # Property to store the dog's name
        self.age = age    # Property to store the dog's age

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

# Subclass of Dog that overrides the bark method
class LoudDog(Dog):
    def bark(self):
        # Overriding the bark method to make it louder
        print(f"{self.name} says WOOF WOOF!")

# Example usage
if __name__ == "__main__":
    regular_dog = Dog("Buddy", 5)
    loud_dog = LoudDog("Max", 3)

    regular_dog.bark()  # Outputs: Buddy says woof!
    loud_dog.bark()     # Outputs: Max says WOOF WOOF!
    loud_dog.birthday() # Outputs: Max is now 4 years old.
```

### Polymorphism

Polymorphism is an object-oriented programming concept that allows different classes to use the same interface but provide different implementations. This means that different types of objects can be handled in a uniform way as long as they implement the interface or method. By using polymorphism, we can make code more flexible and easier to maintain, since the same methods can be used in different contexts with different behaviour.

```
class Dog:
    def __init__(self, name, age):
        self.name = name  # Property to store the dog's name
        self.age = age    # Property to store the dog's age

    def speak(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

class Cat:
    def __init__(self, name, age):
        self.name = name  # Property to store the cat's name
        self.age = age    # Property to store the cat's age

    def speak(self):
        print(f"{self.name} says meow!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

def animal_speak(animal):
    # This function demonstrates polymorphism
    # It can accept any object that has a speak method
    animal.speak()

# Creating instances of Dog and Cat
dog1 = Dog("Buddy", 5)
cat1 = Cat("Whiskers", 3)

# Demonstrating polymorphism
animal_speak(dog1)
animal_speak(cat1)
```

### `isinstance()` and `issubclass()`

`isinstance()` and `issubclass()` are built-in Python functions that are used to determine whether an object is an instance of a class (or a descendant of a class), or whether a class is a descendant of another class.

```
class Fruit:
    pass

class Apple(Fruit):
    pass

apple = Apple()

print(isinstance(apple, Apple))  # True
print(isinstance(apple, Fruit))  # True, because Apple is a subclass of Fruit
print(isinstance(apple, (list, tuple)))  # False, apple is neither a list nor a tuple
```

```
class Fruit:
    pass

class Apple(Fruit):
    pass

class Banana(Fruit):
    pass

print(issubclass(Apple, Fruit))  # True
print(issubclass(Banana, Fruit))  # True
print(issubclass(Fruit, Apple))  # False, Fruit is not a subclass of Apple
print(issubclass(Apple, (Fruit, Banana)))  # True, Apple is a subclass of Fruit
```

### Dunder Methods or Magic Methods

In Python, the so-called "magic methods" or "dunder" (double underscore) methods are special methods that have predefined names and start and end with double underscores (e.g. `__init__, __str__, __repr__`). These methods are called automatically by the Python interpreter during certain operations, such as initializing an object, creating string representations of objects, or defining the behavior of operators.

```
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

    # String representation of the object
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    # Developer-friendly string representation of the object
    def __repr__(self):
        return f"Dog(name='{self.name}', age={self.age})"

    # Equality check between two dogs
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    # Adding two dogs (example purpose)
    def __add__(self, other):
        # Assuming adding ages makes sense here, just for demonstration
        return Dog(f"{self.name}&{other.name}", self.age + other.age)

# Example for use
dog1 = Dog("Rex", 5)
dog2 = Dog("Woof", 7)
print(dog1)  # Calls __str__
print(repr(dog2))  # Calls __repr__
print(dog1 == dog2)  # Calls __eq__, returns False
new_dog = dog1 + dog2  # Calls __add__
print(new_dog)  # Should print the new dog's name as "Rex&Woof" and age as 12
```

### Method Resolution Order (MRO)

***Method Resolution Order (MRO)*** is the algorithm that determines the order in which methods of a class are searched for in object-oriented programming, especially in Python when it comes to inheritance. The MRO determines how the Python interpreter decides which class method to call when a method is called through an object, especially when there is multiple inheritance and methods with the same name can be found in multiple ancestor classes.

```
class A:
    def who_am_i(self):
        print("A")

class B(A):
    def who_am_i(self):
        print("B")

class C(A):
    def who_am_i(self):
        print("C")

class D(B, C):
    pass

# Create an instance of D
d = D()
d.who_am_i()  # This will determine which method is called based on MRO

# Print the Method Resolution Order
print(D.mro())
```

### Operator Overloading 

Operator overloading is a programming technique that allows you to customize the behavior of predefined operators (such as +, -, *, /, etc.) with your own objects. This means that the same operators can be used within different types of data or objects, but can perform different operations in different contexts.

```
class Vector:
    def __init__(self, *components):
        self.components = components  # A tuple that stores vector components
    
    def __add__(self, other):
        # Adding corresponding components of two vectors
        added = tuple(a + b for a, b in zip(self.components, other.components))
        return Vector(*added)
    
    def __sub__(self, other):
        # Subtracting corresponding components of two vectors
        subtracted = tuple(a - b for a, b in zip(self.components, other.components))
        return Vector(*subtracted)
    
    def __repr__(self):
        return f"Vector{self.components}"

# Example usage
v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

# Add two vectors
v3 = v1 + v2
print(v3)  # Output: Vector(4, 6, 8)

# Subtract two vectors
v4 = v2 - v1
print(v4)  # Output: Vector(2, 2, 2)
```