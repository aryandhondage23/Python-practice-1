# The basic idea of object-oriented programming (OOP) in Python is to use classes and objects to represent real-world concepts and entities.

# A class is a blueprint or template for creating objects. It defines the properties and methods that an object of that class will have. Properties are the data or state of an object, and methods are the actions or behaviors that an object can perform.

# An object is an instance of a class, and it contains its own data and methods. For example, you could create a class called "Person" that has properties such as name and age, and methods such as speak() and walk(). Each instance of the Person class would be a unique object with its own name and age, but they would all have the same methods to speak and walk.


def hello():
  print("hello")

hello()
sales1 = 6000
profit1 = 2000
ad1 = 1000
# rajeev.sales

sales2 = 6000
profit2 = 2000
ad2 = 1000 
# vikrant.sales

sales3 = 6000
profit3 = 2000
ad3 = 1000




# Python Class and Objects
# A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.

# Creating a Class:
# Let us now create a class using the class keyword.

class Details:
    name = "Rohan"
    age = 20

# Creating an Object:
# Object is the instance of the class used to access the properties of the class Now lets create an object of the class.



# Example:
obj1 = Details() 
# Now we can print values:

# Example:
class Details:
    name = "Rohan"
    age = 20

obj1 = Details()
print(obj1.name)
print(obj1.age)
# Output:
# Rohan
# 20