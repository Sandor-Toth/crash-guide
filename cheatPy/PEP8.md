## Indentation

Use 4 spaces per indentation level.

```
# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# More indentation included to distinguish this from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

When the conditional part of an if-statement is long enough...

```
# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()

# Closing brace/bracket/parenthesis
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]

my_list = [
    1, 2, 3,
    4, 5, 6,
]
```

## Maximum Line Length

The Python standard library is conservative and requires limiting lines to 79 
characters (and docstrings/comments to 72).
```
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

Following the tradition from mathematics usually results in more readable code:
```
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

## Blank lines

```
import sys

# Surround top-level function and class definitions with two blank lines

class MyClass:
    def __init__(self):
        pass

    def my_method(self):
        pass

    # Method definitions inside a class are surrounded by a single blank line

# There are two blank lines between the class and the following function definition

def top_level_function():
    pass

# There are two empty lines between the functions

def another_top_level_function():
    pass
```
Use empty lines within functions, moderately, to indicate logical sections.

```
def complex_function():
    setup_part = setup()


    main_execution_part = execute(setup_part)


    finalization_part = finalize(main_execution_part)

    return finalization_part
```

## Imports

```
import os
import sys
from subprocess import Popen, PIPE

# Absolute imports are recommended
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

# It’s usually okay to spell this
from myclass import MyClass
from foo.bar.yourclass import YourClass
```

## Whitespace in Expressions and Statements
Avoid extraneous whitespace in the following situations:
```
spam(ham[1], {eggs: 2})

foo = (0,)

if x == 4: print x, y; x, y = y, x

ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

spam(1)
dct['key'] = lst[index]
x = 1
y = 2
long_variable = 3
```

### Documentation Strings
```
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""

class Greeter:
    
    A class for creating objects that can greet users.

    Attributes:
        name (str): The name of the entity doing the greeting.
    
    Methods:
        greet(): Returns a greeting message.
    

    def __init__(self, name):
        
        Initializes a new Greeter instance with the specified name.

        Parameters:
            name (str): The name of the entity doing the greeting.
        
        self.name = name

    def greet(self):
        
        Return a friendly greeting message.
        
        return f"Hello, {self.name}!"
```

### Names

Modules should have short, all-lowercase names.
Underscores can be used in the module name if it improves readability.

`import mymodule`

Function names should be lowercase, with words separated by 
underscores as necessary to improve readability.
Variable names follow the same convention as function names.
```        
my_variable = 10

def my_function():
    pass
```

If a method is non-public, it should have a leading underscore. 
```
def _internal_function():
    pass
```

Class names should normally use the CapWords convention.
```
class MyClass:
    pass
```

Constants are usually defined on a module level and
written in all capital letters with underscores separating words.

`MAX_OVERFLOW = 100`

Starting a Boolean variable with is or has makes it more readable.

```
is_active = True
can_access = False
has_heartbeat = False
```

As collections are buckets of variables, 
it is a good idea to name them in a plural format, as illustrated here:

```
class Patient:
    admitted_patients = ['John','Peter']
```

The name of the dictionary is recommended to be as explicit as possible.

```
persons_cities = {'Imran': 'Ottawa', 'Steven': 'Los Angeles'}
```

### Import conventions
TPython community has developed a convention for aliases
that are used for commonly used packages.
```
# import numpy as np
# import pandas as pd
# import seaborn as sns
# import statsmodels as sm
# import matplotlib.pyplot as plt 
```

There are a couple of tools that can be used to test
how closely your code conforms to PEP 8 guidelines.
```
# pip install pylint
# pip install pep8
```

As Python code is dependent on external packages, keeping track of 
their names and versions is part of automating the build process. 
A good practice is to list all these packages 
in a file named requirements.txt.
```
# pip freeze > requirements.txt
# install -r requirements.txt
```

### Other Recommendations

If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator.

```
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```

Don’t use spaces around the = sign when used to indicate a keyword argument or a default parameter value.

```
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
```

Function annotations should use the normal rules for colons and always have spaces around the -> arrow if present.

```
def munge(input: AnyStr): ...
def munge() -> AnyStr: ...
```

When combining an argument annotation with a default value, use spaces around the = sign.

```
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
```

Compound statements (multiple statements on the same line) are generally discouraged.

```
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()
```

When to use trailing commas:
```
FILES = ('setup.cfg',)
FILES = [
    'setup.cfg',
    'tox.ini',
]
initialize(FILES,
           error=True,
)
```