# Lambda Functions in Python
# In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

lambda arguments: #expression
# Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

# Here is an example of how to use a lambda function:
# Function to double the input
def double(x):
  return x * 2
# Lambda function to double the input
lambda x: x * 2
# The above lambda function has the same functionality as the double function defined earlier. However, the lambda function is anonymous, as it does not have a name.



# Lambda functions can have multiple arguments, just like regular functions. Here is an example of a lambda function with multiple arguments:
# Function to calculate the product of two numbers
def multiply(x, y):
    return x * y
# Lambda function to calculate the product of two numbers
lambda x, y: x * y
# Lambda functions can also include multiple statements, but they are limited to a single expression. For example:

# Lambda function to calculate the product of two numbers,
# with additional print statement
lambda x, y: print(f'{x} * {y} = {x * y}')
# In the above example, the lambda function includes a print statement, but it is still limited to a single expression.









# Map, Filter and Reduce
# In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments.

# map
# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax:

map(function, iterable)
# The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

# Here is an example of how to use the map function:
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Double each number using the map function
doubled = map(lambda x: x * 2, numbers)
# Print the doubled numbers
print(list(doubled))
# In the above example, the lambda function lambda x: x * 2 is used to double each element in the numbers list. The map function applies the lambda function to each element in the list and returns a new list containing the doubled numbers.



# filter
# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. The filter function has the following syntax:

filter(predicate, iterable)
# The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

# Here is an example of how to use the filter function:
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Get only the even numbers using the filter function
evens = filter(lambda x: x % 2 == 0, numbers)
# Print the even numbers
print(list(evens))
# In the above example, the lambda function lambda x: x % 2 == 0 is used to filter the numbers list and return only the even numbers. The filter function applies the lambda function to each element in the list and returns a new list containing only the even numbers.



# reduce
# The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax:

reduce(function, iterable)
# The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple.

# The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result.

# Here is an example of how to use the reduce function:
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]
# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)
# Print the sum
print(sum)