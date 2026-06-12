# 16)f-string
# It is a new string formatting mechanism introduced by the PEP 498.
# When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.") 

name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")  

print(f"{2 * 30}")  




# 17)Docstring
# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)


def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__) #we can use string comment as output like normal comment we cant take as input




# 17)Recursion
# In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = 7; 
print("Number: ",num)
print("Factorial: ",factorial(num))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 8

print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i), end=" , ")