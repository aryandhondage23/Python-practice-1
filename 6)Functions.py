# A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.
# 1.Built-in functions
# 2.User-defined functions

# i)Built-in functions
# Python has many built-in functions that we can use without needing to define them. Some examples include:

# print() - used to display output to the console
# len() - used to get the length of a string, list, or other iterable               
# input() - used to get user input from the console
# type() - used to determine the type of a variable or value

# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.
print(max(10, 20, 30, 5))


# ii)User-defined functions

# We can also create our own functions to perform specific tasks. To define a function, we use the def keyword followed by the function name and parentheses. Inside the parentheses, we can specify any parameters that the function will take. The code block that performs the task is indented below the function definition.
def greet(name):
    print("Hello, " + name + "!")   
greet("Alice")
# In this example, we defined a function called greet that takes one parameter, name. When we call the function with the argument "Alice", it prints a greeting message to the console.
# We can also return values from a function using the return statement. This allows us to use the output of the function in other parts of our program.

def even():
  for i in range(10):
    if i%2==0:
      print(i," is Even")
    else:
      print(i," is Odd")

even()

# Default arguments: We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.
def average(a=2,b=5):
  print("average of Number: ",a+b/2)
average()

# Keyword arguments: We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.
def average(a,b):
  print("average of Number: ",a+b/2)    
average(b=10,a=5)

# Required arguments: In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.
# Example 1: when number of arguments passed does not match to the actual function definition.
def average(a,b,c):
  print("average of Number: ",a+b/2)
average(5,10) # This will raise an error because we are missing the required argument 'c' in the function call.

# Example 2: when number of arguments passed matches to the actual function definition.
def average(a,b,c):
  print("average of Number: ",a+b/2)
average(4,5,6)


# Variable-length arguments: Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

# i)Arbitrary Arguments(args):
# While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.
def name(*name):
  print(type(name))
  print("Hello,", name[0], name[1], name[2])
name("James", "Buchanan", "Barnes")


# ii)Keyword Arguments(kwargs):
# While creating a function, pass a ** before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.
def name(**name):
  print(type(name))
  print("Hello,", name["first"], name["middle"], name["last"])
name(first="James", middle="Buchanan", last="Barnes")

# iii) return Statement:
# The return statement is used to return the value of the expression back to the calling function
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))
