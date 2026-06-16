# Python Dictionaries
# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
Output:
{'name': 'Karan', 'age': 19, 'eligible': True}


# Accessing Dictionary items:
# I. Accessing single values:
# Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))
# Output:
Karan
True


# II. Accessing multiple values:
# We can print all the values in the dictionary using values() method.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())
# Output:
dict_values(['Karan', 19, True])


# III. Accessing keys:
# We can print all the keys in the dictionary using keys() method.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())
# Output:
dict_keys(['name', 'age', 'eligible'])
 
 
# IV. Accessing key-value pairs:
# We can print all the key-value pairs in the dictionary using items() method.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())
# Output:
dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])





# Dictionary Methods
# Dictionary uses several built-in methods for manipulation.They are listed below

# update()
# The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)
# Output:
{'name': 'Karan', 'age': 19, 'eligible': True}
{'name': 'Karan', 'age': 20, 'eligible': True, 'DOB': 2001}
# Removing items from dictionary:
# There are a few methods that we can use to remove items from dictionary.


# clear():
# The clear() method removes all the items from the list.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)
# Output:
{}


# pop():
# The pop() method removes the key-value pair whose key is passed as a parameter.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)
# Output:
{'name': 'Karan', 'age': 19}


# popitem():
# The popitem() method removes the last key-value pair from the dictionary.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)
# Output:
{'name': 'Karan', 'age': 19, 'eligible': True}


# del:
# we can also use the del keyword to remove a dictionary item.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)
# Output:
{'name': 'Karan', 'eligible': True, 'DOB': 2003}

# If key is not provided, then the del keyword will delete the dictionary entirely.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)
# Output:
# NameError: name 'info' is not defined










# Python - else in Loop
# As you have learned before, the else clause is used along with the if statement.

# Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.

# Syntax
for counter in sequence:
    #Statements inside for loop block
else:
    #Statements inside else block


# Example:
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")
# Output:
iteration no 1 in for loop
iteration no 2 in for loop
iteration no 3 in for loop
iteration no 4 in for loop
iteration no 5 in for loop
# else block in loop
# Out of loop




# Exception Handling
# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

# Exceptions in Python
# Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

# When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

# Python try...except
# try….. except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

# Syntax:
try:
     #statements which could generate 
     #exception
except:
     #Soloution of generated exception


# Example:
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
# Output:
Enter an integer: 6.022
Number entered is not an integer.