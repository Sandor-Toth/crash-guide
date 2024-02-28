## OOP - Object-Oriented Programming

### What is OOP?

OOP, or object-oriented programming, is a programming paradigm that uses objects to organise and structure code. This approach helps to make programs easier to understand, maintain and extend.

### What do we use OOP for?

- ***Software development:*** OOP makes it easier to design and implement complex software systems.
Object-oriented programming allows code to be reused in different projects through inheritance and composition.
- ***Modularity:*** OOP promotes modularity, allowing developers to develop separate modules or objects that can be easily integrated into other projects.

### What should we not use OOP for?
- ***Simple scripts or programs:*** if the task is simple and does not require complex data structures or behaviours, OOP may be too complex.
- ***Performance-critical systems:*** In some cases where performance is the most important consideration (e.g. time-critical systems), the overhead of OOP may be a disadvantage.

### What is a class?
A class is a template that defines the state (data members, properties) and behaviour (methods) of an object. Classes are used to create objects.

### What are object and methods?
- ***Object:*** an instance of a class. It contains the data and behaviours defined by that class.
- ***Methods:*** Functions that define the behaviour of an object and that access and modify the state (data members) of the object.

### What is the difference between methods and functions?

- ***Methods:*** Class-bound functions that can only be accessed through a specific object or class, and usually have access to the object's data members.

- ***Functions:*** Independent functions that can perform operations on any type of data and are not tightly bound to a specific object or class.


### Example: Class and Object
```
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"brand: {self.brand}, model: {self.model}")

# Create an object
car1 = Car("Toyota", "Corolla")
car1.display_info()
```

The keyword `self` refers to the current instance (object). When a method is called on an object, Python automatically passes the object as the first parameter to the method. This parameter is called "self" to indicate that it refers to the current instance of the class.

The purpose of using `self` is to allow the object's attributes and other methods to be referenced within the class.

The `__init__` method serves as the class constructor, which is automatically called when a new object is instantiated from the class. The purpose of the `__init__` method is to initialize the object, i.e., to set up the attributes and the initial state that the object requires at the moment of its creation.

### Example: Methods vs Functions

```
# Method inside a class
class Calculator:
    def add(self, a, b):
        return a + b

# Function outside a class
def add(a, b):
    return a + b

# Using the method
calculator = Calculator()
print(calculator.add(5, 3))

# Using the function
print(add(5, 3))
```

### Create class with OOP

```
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def book_info(self):
        return f"{self.title} by {self.author}, {self.pages} pages long."

# Creating an instance of the Book class
my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 200)

# Accessing the book_info method to get information about my_book
print(my_book.book_info())
print(my_book.title)
print(my_book.author)
print(my_book.pages)

my_book2 = Book("A Game of Thrones", "George R. R. Martin", 694)
print(my_book2.book_info())
print(my_book2.title)
print(my_book2.author)
print(my_book2.pages)
```

```
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percentage):
        """Apply a discount to the product's price."""
        if 0 < percentage < 100:  # Ensures the discount is between 0 and 100%
            discount_amount = (percentage / 100) * self.price
            self.price -= discount_amount
        else:
            print("Invalid discount percentage.")

    def display_info(self):
        """Display the product's information."""
        return f"Product: {self.name}, Price: ${self.price:.2f}"

# Creating an instance of the Product class
product1 = Product("Laptop", 1200)

# Displaying product information before applying the discount
print(product1.display_info())

# Applying a 20% discount to the product's price
product1.apply_discount(20)

# Displaying product information after applying the discount
print(product1.display_info())
```

### Class Variables

A class variable in Python is a variable that is shared among all instances of a class. Class variables are defined within the class construction but outside any of the instance methods. Class variables are not unique to each instance; rather, they are shared across all instances of the class, meaning that if you change the value of a class variable for one instance, it changes for all instances.

```
class Employee:
    # Class variable
    raise_amount = 1.04  # 4% raise
    emp_counter = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last    
        self.pay = pay 
        # Counting the number of employees
        Employee.emp_counter += 1

    def apply_raise(self):
        # Using the class variable to apply a raise to the instance's salary
        self.pay = int(self.pay * self.raise_amount)

# Creating instances
emp_1 = Employee('John', 'Doe', 50000)
print(Employee.emp_counter) # 1
emp_2 = Employee('Jane', 'Doe', 60000)
print(Employee.emp_counter) # 2

# Initial salary
print(emp_1.pay)  # 50000
print(emp_2.pay)  # 60000

# Applying raise
emp_1.apply_raise()
emp_2.apply_raise()

# New salary
print(emp_1.pay)  # 52000
print(emp_2.pay)  # 62400

# Modifying class variable
Employee.raise_amount = 1.05

# Applying raise again with the modified value
emp_1.apply_raise()
emp_2.apply_raise()

# New salary with the modified class variable value
print(emp_1.pay)  # 54600
print(emp_2.pay)  # 65520
```

### What is `__dict__ `?

`__dict__` is a special attribute in Python, available in most objects. It contains a dictionary that maps attribute names to their values. This feature is highly useful for several reasons:

- ***Inspecting Object State:*** It allows for the inspection of an object's state at any point in time, showing all the attributes currently bound to the object and their values.
- ***Dynamic Attribute Management:*** Python's dynamic nature is showcased through the ability to add, modify, or remove attributes from objects at runtime, which can be directly observed through changes in the `__dict__` attribute.
- ***Debugging:*** It can be particularly useful for debugging purposes, as it gives a clear view of what data an object is holding at any given moment.

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance
person = Person("John Doe", 30)

# Printing initial state
print("Initial state:", person.__dict__)

# Modifying attributes
person.name = "Jane Doe"
person.age = 32

# Printing modified state
print("Modified state:", person.__dict__)

# Adding a new attribute
person.email = "janedoe@example.com"

# Printing expanded state with the new attribute
print("Expanded state:", person.__dict__)
```

### What are `@property` and `@staticmethod`?

The `@property` decorator allows you to call a method of a class as an attribute. This means that when you access the method, you do not need to use parentheses. 

The `@property` decorator is often used to treat the attributes of a class as "read-only" properties, allowing you to retrieve their values but preventing you from modifying them directly. Methods with the `@staticmethod` decorator are functions that are logically linked to the class, but have no access to the state of either the class (cls) or the instance (self).

```
class Circle:
    pi = 3.14159  # Class variable for the value of pi

    def __init__(self, radius) -> None:
        self.radius = radius

    @property
    def diameter(self):
        """Calculates and returns the diameter of the circle."""
        return self.radius * 2

    @property
    def area(self):
        """Calculates and returns the area of the circle."""
        return self.pi * (self.radius ** 2)

    @staticmethod
    def info():
        """Returns a general information string about circles."""
        return "A circle is a simple shape in Euclidean geometry."
        
# Example usage
circle = Circle(5)
# Calls the @property method to get the circle's diameter
print(circle.diameter)  
# Calls the @property method to get the circle's area
print(circle.area)  
# Calls the @staticmethod to get general info about circles
print(Circle.info())  
```

### Class Methods

Methods with the `@classmethod` decorator are used as methods defined at the class level that access the state of the class, but not the state of a particular instance. The `@classmethods` are given the class itself as their first parameter (conventionally called cls), which allows them to access the attributes of the class and other class methods. 

- ***Alternative Constructors***: The most common use is to create alternative constructors. Since the `__init__` method only allows one type of initialization, `@classmethods` can be used to define different initialization logic. For example, if you want to create an instance of a class from multiple sources (e.g., a text file, a database, or a data structure), you can define a separate class method for each source type.

- ***Static Methods vs. Class Methods***: Although methods with the `@staticmethod` decorator work similarly in the sense that they do not access the state of a particular instance, class methods have the advantage of accessing and modifying the state of the class. This allows class-level data to be managed and modified through instances of the class.

- ***Class-level logic***: `@classmethods` can be used to implement class-level logic that is not tightly bound to any single instance. For example, if a class handles the number of instances created or other class-level data, a class method is a great way to handle it.

- ***Inheritance Support***: Class methods can also be useful in inheritance hierarchies, as they allow descendant classes to have their own implementations without overriding the methods of the original class. This is a form of polymorphism that provides greater flexibility in interactions between classes.

```
class Employee:
    num_of_employees = 0  # Class variable to keep track of the number of employees

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        # Increment the number of employees for each instantiation
        Employee.num_of_employees += 1  

    @classmethod
    def from_string(cls, employee_str):
        """An alternative constructor that creates an Employee instance from a string.
        The format of the string should be 'LastName FirstName Pay'."""
        first_name, last_name, pay = employee_str.split(' ')
        # Creates a new Employee instance
        return cls(first_name, last_name, int(pay))  

    @classmethod
    def print_num_of_employees(cls):
        """Prints the current number of employees."""
        print(f"Currently, there are {cls.num_of_employees} employees.")

# Instantiating using the __init__ method
emp_1 = Employee('Jane', 'Doe', 50000)
print(emp_1.__dict__)

# Instantiating using the alternative constructor
emp_str = 'John Doe 60000'
emp_2 = Employee.from_string(emp_str)
print(emp_2.__dict__)

# Printing the number of employees
Employee.print_num_of_employees()
```

### Static method vs `@classmethod`

The example below illustrates the use of both instance methods and a @classmethod to demonstrate their differences and how they can be used together within a class. 

```
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_dict(cls, book_dict):
        """Class method to create a Book instance from a dictionary."""
        return cls(book_dict['title'], book_dict['author'])

    @staticmethod
    def display_info():
        """Static method to display general information about books."""
        print("Books are an excellent source of knowledge and entertainment.")

# Creating a book instance using the __init__ method
book1 = Book('To Kill a Mockingbird', 'Harper Lee')

# Creating a book instance using the class method from_dict
book_dict = {'title': '1984', 'author': 'George Orwell'}
book2 = Book.from_dict(book_dict)

# Printing the book instances to show they were created successfully
# Output: {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
print(book1.__dict__)
# Output: {'title': '1984', 'author': 'George Orwell'}
print(book2.__dict__)  

# Using the static method
# Output: Books are an excellent source of knowledge and entertainment.
Book.display_info()  
```

```
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def format_time(self):
        """Instance method to format time into HH:MM:SS pattern."""
        return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"

    @classmethod
    def from_string(cls, time_str):
        """Class method to create a Time instance from a string with HH:MM:SS or HH/MM/SS format."""
        import re
        time_data = re.findall(r'\d{2}:\d{2}:\d{2}|\d{2}/\d{2}/\d{2}', time_str)[0]
        list_time = time_data.replace('/', ':').split(':')
        print(list_time)
        hours, minutes, seconds = list_time
        return cls(int(hours), int(minutes), int(seconds))

    @staticmethod
    def convert_24_to_12_hour_format(time_str):
        """Static method to convert time from 24-hour format to 12-hour format."""
        hours, minutes, seconds = time_str.split(':')
        hours = int(hours)
        am_pm = "AM" if hours < 12 else "PM"
        hours = hours % 12
        hours = 12 if hours == 0 else hours
        return f"{hours}:{minutes}:{seconds} {am_pm}"
    

# Creating a Time instance using the constructor
time1 = Time(14, 30, 45)
print(time1.format_time())  # Output: 14:30:45

# Creating a Time instance from a string using the class method
time_str = "15/45/30"
time2 = Time.from_string(time_str)
print(time2.format_time())  # Output: 15:45:30

# Converting 24-hour format time to 12-hour format using the static method
print(Time.convert_24_to_12_hour_format("18:25:00")) # Output: 6:25:00 PM
```

`@classmethod` is useful when you need to work with class state or alternative constructs within the class, while `@staticmethod` is ideal for functionality that is related to the class but does not depend on the state of the class or instances.

### Abstraction and Encapsulation

***Abstraction***: Abstraction is a basic principle of OOP that allows developers to show only the details of an object that are necessary for the user, hiding unnecessary details. 

Define an abstract class that represents the general concept or model for a vehicle. This class will define the methods (operations) that each vehicle class will implement.

Then define a class that implements the Vehicle abstract class. This class implements the start and stop abstract methods.

Vehicle is an abstract class, not directly instantiated. Instead, the Car class, which implements the Vehicle class, can be used to instantiate vehicles and use the defined methods.

```
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print(f"{self.brand} {self.model} is starting.")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping.")


my_car = Car("Toyota", "Corolla")

my_car.start()  # Output: Toyota Corolla is starting.
my_car.stop()   # Output: Toyota Corolla is stopping.
```

***Incapsulation***: Encapsulation allows the data members (properties and methods) of a class to be hidden from external access, so that only methods within the class can modify them. This ensures data integrity and security. Encapsulation can be used to control access to data, for example by using public, private and protected modifiers to determine which classes can access this data.

Let's create a BankAccount class that hides the balance data tag and only allows its modification through certain methods.

```
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # A balance attribútumot priváttá tesszük

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} has been deposited. New balance is: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} has been withdrawn. New balance is: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance


# Create a BankAccount object with an initial balance
my_account = BankAccount(1000) # Initial balance: 1000

# Deposit to the account
my_account.deposit(500) # 500 has been deposited. New balance is: 1500

# Withdraw money from the account
my_account.withdraw(200) # 200 has been withdrawn. New balance is: 1300

# Query balance
current_balance = my_account.get_balance()
print(f"Current balance: {current_balance}") # Current balance: 1300

# AttributeError: 'BankAccount' object has no attribute '__balance'.
# print(my_account.__balance)
```
### Inheritance

Inheritance in programming, especially in object-oriented programming, is a way to create new classes based on existing classes. A new class (derived class or child class) inherits the properties and methods of the parent class (base class or parent class), while it can also add new properties and methods or modify the behaviour of inherited methods.

```
class Device:  # Base Class / Parent Class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Device: {self.brand} {self.model}"

class Laptop(Device):  # Derived Class / Child Class
    def __init__(self, brand, model, ram, storage):
        # Call the constructor of the parent class
        super().__init__(brand, model)
        self.ram = ram
        self.storage = storage

    def laptop_info(self):
        return f"{self.device_info()}, RAM: {self.ram}, Storage: {self.storage}"

laptop1 = Laptop('Dell', 'XPS 15', '16GB', '1TB SSD')
print(laptop1.laptop_info())
```
### Multilevel inheritance

Multilevel inheritance in object-oriented programming refers to a hierarchy where a class is derived from another class, which is itself derived from another class. This hierarchy allows the inheritance of properties and methods through multiple levels.

```
class Vehicle:  # Base Class / Parent Class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def vehicle_info(self):
        return f" Vehicle: {self.brand} {self.model}\n"

class Car(Vehicle):  # Derived Class
    def __init__(self, brand, model, horsepower):
        super().__init__(brand, model)
        self.horsepower = horsepower

    def car_info(self):
        return f"{self.vehicle_info()} Horsepower: {self.horsepower}\n"

class ElectricCar(Car):  # Further Derived Class
    def __init__(self, brand, model, horsepower, battery_capacity):
        super().__init__(brand, model, horsepower)
        self.battery_capacity = battery_capacity

    def electric_car_info(self):
        return f"{self.car_info()} Battery Capacity: {self.battery_capacity} kWh"

electric_car1 = ElectricCar('Tesla', 'Model S', 670, 100)
print(electric_car1.electric_car_info())
```

### Method Resolution Order (MRO)

Method Resolution Order (MRO) is the algorithm that determines the order in which methods of a class are searched for in object-oriented programming, especially in Python when it comes to inheritance. The MRO determines how the Python interpreter decides which class method to call when a method is called through an object, especially when there is multiple inheritance and methods with the same name can be found in multiple ancestor classes.

```
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.__mro__)
# OR
print(D.mro())
```
### Method Overriding

Method Overriding is an object-oriented programming technique that allows you to change the behavior of a method defined in a base class to a method defined in a child class. This means that if you rewrite a method in a descendant class that already exists in the parent class, the rewritten method will run when called on an instance of the descendant class. This may be useful when the generic behavior of the parent class is not appropriate for the specific needs of the descendant class and there is a need to fine-tune the behavior or to specify completely new behavior.

```class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working on general tasks.")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def work(self):
        # Overriding the work method to show a developer-specific task
        print(f"{self.name} is coding in {self.programming_language}.")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def work(self):
        # Overriding the work method to show a manager-specific task
        print(f"{self.name} is managing the {self.department} department.")

# Creating instances of each class
general_employee = Employee("John Doe", 50000)
developer = Developer("Jane Doe", 80000, "Python")
manager = Manager("Mike Smith", 100000, "IT")

# Invoking the work method for each instance
general_employee.work()  # Calls the base class method
developer.work()         # Calls the overridden method in Developer class
manager.work()           # Calls the overridden method in Manager class
```

### `isinstance()` and `issubclass()`

`isinstance()` and `issubclass()` are built-in Python functions that are used to determine whether an object is an instance of a class (or a descendant of a class), or whether a class is a descendant of another class.

```
class Animal:
    pass

class Bird(Animal):
    pass

class Eagle(Bird):
    pass


eagle_instance = Eagle()

# Use isinstance

# True, because eagle_instance is an instance of Eagle
print(isinstance(eagle_instance, Eagle))
# True, because Eagle is a descendant of Bird
print(isinstance(eagle_instance, Bird))
# True, because Eagle is a descendant of Animal
print(isinstance(eagle_instance, Animal))


# use issubclass
# True, because Bird is a descendant of Animal
print(issubclass(Bird, Animal))
# True, because Eagle is a descendant of Bird
print(issubclass(Eagle, Bird)) 
# False, because Animal is not descended from Bird
print(issubclass(Animal, Bird))
```

### Naming conventions

In Python, naming conventions for variables and methods play an important role in controlling the visibility and accessibility of data members. 

One Underscore (_)
Use the _ (one underscore) prefix to mark data members or methods as "protected" or for internal use. This is a convention among Python programmers and does not prevent access to data members, it merely indicates that they are not intended for direct access from outside. 

Two Underscores (__)
The use of the __ (two underscores) prefix is used to hide data members or methods. This activates the so-called "name mangling" mechanism in Python, which makes it difficult to access data members directly from outside the class.

```
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        # Single underscore: Indicates 'protected' member; meant for internal use.
        self._discount = 5

    def apply_discount(self):
        # Applying the 'protected' discount to the price
        discounted_price = (self.price / 100) * self._discount
        final_price = self.price - discounted_price
        return final_price

class AdvancedPhone(Phone):
    def __init__(self, brand, model, price, extra_feature):
        super().__init__(brand, model, price)
        # Double underscore: This attribute is name-mangled to avoid accidental access or override.
        self.__extra_feature = extra_feature

    def get_extra_feature(self):
        return self.__extra_feature

phone = Phone("GenericBrand", "ModelX", 300)
# Accessing the method that uses the 'protected' member
print(phone.apply_discount())  

advanced_phone = AdvancedPhone("GenericBrand", "ModelY", 500, "Waterproof")
# Accessing a method that returns a 'private' member
print(advanced_phone.get_extra_feature()) 
# Direct access to '__extra_feature' outside the class would raise an AttributeError:
# print(advanced_phone.__extra_feature)  # This would result in an error

# Accessing the 'protected' _discount variable is possible, but against conventions
print(phone._discount)  # Not recommended
```

### Dunder Methods or Magic Methods

In Python, the so-called "magic methods" or "dunder" (double underscore) methods are special methods that have predefined names and start and end with double underscores (e.g. `__init__, __str__, __repr__`). These methods are called automatically by the Python interpreter during certain operations, such as initializing an object, creating string representations of objects, or defining the behavior of operators.

In this example, the `__str__` method returns a readable string with the title and author of the book, while `__repr__` returns a more precise, formal representation that could be used to recreate the book object. And the `__len__` method allows you to query the number of pages in the book with the len() function, which is another example of customizing dunder methods.

```
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"\"{self.title}\" by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        return self.pages


book = Book("Python Programming", "John Doe", 500)

print(book)  # "Python Programming" by John Doe
print(repr(book))  # Book('Python Programming', 'John Doe', 500)
print(len(book))  # 500
```

### Operator Overloading 

Operator overloading is a programming technique that allows you to customize the behavior of predefined operators (such as +, -, *, /, etc.) with your own objects. This means that the same operators can be used within different types of data or objects, but can perform different operations in different contexts.

```
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Operator overload for addition
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 4)
v2 = Vector(5, -2)

# Add Vector objects by overloading the operator
v3 = v1 + v2

print(v3) # Vector(7, 2)
```

### Polymorphism

Polymorphism is an object-oriented programming concept that allows different classes to use the same interface but provide different implementations. This means that different types of objects can be handled in a uniform way as long as they implement the interface or method. By using polymorphism, we can make code more flexible and easier to maintain, since the same methods can be used in different contexts with different behaviour.

```
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())


dog = Dog()
cat = Cat()

animal_sound(dog)  # Woof!
animal_sound(cat)  # Meow!
```

```
class Shape:
    def draw(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        return f"Drawing a circle with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        return f"Drawing a rectangle with width {self.width} and height {self.height}"

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def draw(self):
        return f"Drawing a triangle with base {self.base} and height {self.height}"

def draw_shape(shape):
    # This function demonstrates polymorphism
    print(shape.draw())

# Creating instances of shapes
circle = Circle(5)
rectangle = Rectangle(10, 15)
triangle = Triangle(7, 9)

# Polymorphic function calls
draw_shape(circle)    # Drawing a circle with radius 5
draw_shape(rectangle) # Drawing a rectangle with width 10 and height 15
draw_shape(triangle)  # Drawing a triangle with base 7 and height 9
```