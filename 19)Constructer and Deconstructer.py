# Constructors
# A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.
# A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.

# Syntax of Python Constructor
def __init__(self):
	# initializations
# init is one of the reserved functions in Python. In Object Oriented Programming, it is known as a constructor.


# Parameterized Constructor in Python
#  When the constructor accepts arguments along with self, it is known as parameterized constructor.
# These arguments can be used inside the class to assign the values to the data members.

# Example:
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")
# Output:
# Crab belongs to the Crustaceans group.



# Default Constructor in Python
# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.

# Example:
class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details()
# Output:
# animal Crab belongs to Crustaceans group








# Python Decorators
# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.
# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:

@decorator_function
def my_function():
    pass
# The @decorator_function notation is just a shorthand for the following code:

def my_function():
    pass
my_function = decorator_function(my_function)
# Decorators are often used to add functionality to functions and methods, such as logging, memoization, and access control.



# Practical use case
# One common use of decorators is to add logging to a function. For example, you could use a decorator to log the arguments and return value of a function each time it is called:

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b
# In this example, the log_function_call decorator takes a function as an argument and returns a new function that logs the function call before and after the original function is called.