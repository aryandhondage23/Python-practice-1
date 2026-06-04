#2)Variables and Data Type? 
#Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:

a = 1
b = True
c = "Aryan"
d = None
print(a,b,c,d)

#Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error. In python, we can print the type of any operator using type function:

a = 1
b = True
c = "Aryan"
d = None
print(type(a),type(b),type(c),type(d))

#1. Numeric data: int, float, complex int: 3, -8, 0 float: 7.349, -9.0, 0.0000001 complex: 6 + 2i

#2. Text data: str str: "Hello World!!!", "Python Programming"

#3. Boolean data: Boolean data consists of values True or False.

#4. Sequenced data:
#   list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.
my_list = [1, 2, 3, "Hello", True]
print(my_list)

#   tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and cannot be modified after creation.
my_tuple = (1, 2, 3, "Hello", True)
print(my_tuple)

#   range: A range is a sequence of numbers that is commonly used for looping a specific number of times in for loops. It is defined using the range() function.
my_range = range(1, 10)     
print(my_range)

#5. Mapping data: dict A dictionary is an unordered collection of key-value pairs enclosed within curly braces. Each key is unique and maps to a specific value.
my_dict = {"name": "Aryan", "age": 20, "is_student": True}
print(my_dict)  

#Typcasting: Typecasting is the process of converting a variable from one data type to another. In Python, we can use built-in functions like int(), float(), str(), bool() etc. to perform typecasting.
#implicit typecasting: This is when Python automatically converts one data type to another without the programmer's intervention. For example, when we add an integer and a float, Python will automatically convert the integer to a float before performing the addition.
a = 5   
b = 3.2
result = a + b
print(result)  # Output: 8.2

##explicit typecasting: This is when the programmer explicitly converts a variable from one data type to another using built-in functions. For example, if we want to convert a string to an integer, we can use the int() function.
# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))
