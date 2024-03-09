Error and exception handling in Python is critical to writing robust and fault-tolerant programs. Python categorises errors into two main types: syntax errors and exceptions. Syntax errors, as the name suggests, are errors in the syntax of Python code. Exceptions, on the other hand, are errors detected during execution, and Python provides mechanisms for handling them gracefully.

### Common Runtime Errors (Exceptions) in Python

- ***IndexError***: Occurs when an attempt is made to access an element with an invalid index.
- ***ModuleNotFoundError***: Thrown if a specified module cannot be found.
- ***ZeroDivisionError***: Occurs when a number is divided by zero.
- KeyError***: Occurs when a dictionary is accessed with an invalid key.
- ***StopIteration***: Raised by the `__next__()` method of an iterator when there are no more elements.
- ***TypeError***: Occurs when an operation or function is applied to an object of an inappropriate type.

### Working with Exceptions

To handle exceptions, Python uses the `try' and `except' blocks. Code that could throw an exception is placed in the `try' block. When an exception occurs, control is passed to the `except' block. Multiple `except` blocks can be used to specifically handle different exceptions.

```
try:
    # Attempt to execute code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle specific exception
    print(`You can't divide by zero!`)
```

You can also catch multiple exceptions in a single block or use a generic `except` block to catch any exception. It's also possible to access the error message associated with the exception using `as e`.

### Raising Exceptions

Python allows you to explicitly `raise' exceptions using the raise keyword. This can be useful if you need to enforce certain conditions in your code.

```
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)
```

### Defining Custom Exceptions

You can define custom exceptions by creating a new class derived from the built-in Exception class or one of its subclasses.

```
class NegativeNumberError(Exception):
    """Exception raised for errors in the input, negative numbers not allowed."""
    pass

def sqrt(value):
    if value < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number")
    return value ** 0.5

try:
    print(sqrt(-1))
except NegativeNumberError as e:
    print(e)
```

### Exception Handling Blocks

- `try`: Block of code to be checked for errors.
- `except`: Block of code to be executed if an error occurs in the try block.
- `else`: Optional block of code to be executed if no errors occur in the try block.
- `finally`: Block that will always be executed after try, except, and else blocks, regardless of whether an exception was thrown. Useful for cleaning up resources such as files or network connections.

```
try:
    f = open("file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found.")
finally:
    f.close()
```

In summary, handling exceptions in Python involves using try, except, and optionally else and finally blocks to handle errors gracefully, ensuring the stability and reliability of your program. You can also define custom exceptions for more specific error handling tailored to the needs of your application.

---