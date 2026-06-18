# Enumerate function in python
# The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)
# The output of this code will be:
0 apple
1 banana
2 mango
# As you can see, the enumerate function returns a tuple containing the index and value of each element in the sequence. You can use the for loop to unpack these tuples and assign them to variables, as shown in the example above.



# Changing the start index
# By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function:

# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
# This will output:
1 apple
2 banana
3 mango

# The enumerate function is often used when you need to loop over a sequence and perform some action with both the index and value of each element. For example, you might use it to loop over a list of strings and print the index and value of each string in a formatted way:
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')
# This will output:
1: apple
2: banana
3: mango
# In addition to lists, you can use the enumerate function with any other sequence type in Python, such as tuples and strings. Here's an example with a tuple:


# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)

# And here's an example with a string:
# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)




# if "__name__ == "__main__" in Python
# The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script.

# In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module. When a Python script is run directly, the __name__ variable is set to the string __main__ When the script is imported as a module into another script, the __name__ variable is set to the name of the module.

# Here's an example of how the if __name__ == __main__ idiom can be used:

def main():
    # Code to be run when the script is run directly
    print("Running script directly")

if __name__ == "__main__":
    main()
# In this example, the main function contains the code that should be run when the script is run directly. The if statement at the bottom checks whether the __name__ variable is equal to __main__. If it is, the main function is called.


# Why is it useful?
# This idiom is useful because it allows you to reuse code from a script by importing it as a module into another script, without running the code in the original script. For example, consider the following script:

def main():
    print("Running script directly")

if __name__ == "__main__":
    main()
# If you run this script directly, it will output "Running script directly". However, if you import it as a module into another script and call the main function from the imported module, it will not output anything:


import script

script.main()  # Output: "Running script directly"
# This can be useful if you have code that you want to reuse in multiple scripts, but you only want it to run when the script is run directly and not when it's imported as a module.


# Is it a necessity?
# It's important to note that the if __name__ == "__main__" idiom is not required to run a Python script. You can still run a script without it by simply calling the functions or running the code you want to execute directly. However, the if __name__ == "__main__" idiom can be a useful tool for organizing and separating code that should be run directly from code that should be imported and used as a module.

# In summary, the if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script. It allows you to reuse code from a script by importing it as a module into another script, without running the code in the original script.









# How importing in python works
# Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.

# To import a module in Python, you use the import statement followed by the name of the module. For example, to import the math module, which contains a variety of mathematical functions, you would use the following statement:

import math
Once a module is imported, you can use any of the functions and variables defined in the module by using the dot notation. For example, to use the sqrt function from the math module, you would write:



import math
result = math.sqrt(9)
print(result)  # Output: 3.0


# from keyword
# You can also import specific functions or variables from a module using the from keyword. For example, to import only the sqrt function from the math module, you would write:
from math import sqrt
result = sqrt(9)
print(result)  # Output: 3.0



You can also import multiple functions or variables at once by separating them with a comma:
from math import sqrt, pi
result = sqrt(9)
print(result)  # Output: 3.0
print(pi)  # Output: 3.141592653589793



# importing everything
# It's also possible to import all functions and variables from a module using the * wildcard. However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from.
from math import *
result = sqrt(9)
print(result)  # Output: 3.0
print(pi)  # Output: 3.141592653589793
# Python also allows you to rename imported modules using the as keyword. This can be useful if you want to use a shorter or more descriptive name for a module, or if you want to avoid naming conflicts with other modules or variables in your code.



# The "as" keyword
import math as m
result = m.sqrt(9)
print(result)  # Output: 3.0
print(m.pi)  # Output: 3.141592653589793



# The dir function
# Finally, Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module.
import math
print(dir(math))
# This will output a list of all the names defined in the math module, including functions like sqrt and pi, as well as other variables and constants.