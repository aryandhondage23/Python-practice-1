# Finally Clause
# The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

# Syntax:
try:
   #statements which could generate 
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation
    
   
# The finally block is executed irrespective of the outcome of try……except…..else blocks
# One of the important use cases of finally block is in a function which returns a value.

# Example:
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")
# Output 1:
# Enter an integer: 19
# Integer Accepted.
# This block is always executed.

# Output 2:
# Enter an integer: 3.142
# Number entered is not an integer.
# This block is always executed.






# Raising Custom errors
# In python, we can raise custom errors by using the raise keyword.

salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
# In the previous tutorial, we learned about different built-in exceptions in Python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exceptions that serve our purpose.



# Defining Custom Exceptions
# In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

# Here's the syntax to define custom exceptions:

class CustomError(Exception):
  # code ...
  pass

try:
  # code ...

except CustomError:
  # code...

# This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.









# If ... Else in One Line
# There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short. Here's an example:

a = 2
b = 330
print("A") if a > b else print("B")
# You can also have multiple else statements on the same line:

# Example
# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# Another Example
result = value_if_true if condition else value_if_false
# This syntax is equivalent to the following if-else statement:

if condition:
    result = value_if_true
else:
    result = value_if_false