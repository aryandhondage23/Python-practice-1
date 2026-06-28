# Inheritance in python
# When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.

# Python Inheritance Syntax
class BaseClass:
#   Body of base class
class DerivedClass(BaseClass):
#   Body of derived class
# Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.



# Single Inheritance:
# Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.

# Example:
class Parent:
    def func1(self):
        print("This function is in parent class.")
 
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
 
object = Child()
object.func1()
object.func2()
Output:
# This function is in parent class.
# This function is in child class.



# Multiple Inheritance:
# When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class.

# Example:
class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
 
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
 
class Son(Mother, Father):
    def parents(self):
        print("Father name is :", self.fathername)
        print("Mother :", self.mothername)
s1 = Son()
s1.fathername = "Mommy"
s1.mothername = "Daddy"
s1.parents()

# Output:
Father name is : Mommy
Mother name is : Daddy



# Multilevel Inheritance :
# In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather.

# Example:
class Grandfather:
 
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
 
 
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()
# Output:
# George
# Grandfather name : George
# Father name : Philip
# Son name : Charles



# Hierarchical Inheritance:
# When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes.

# Example:
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
      
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
 
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
# Output:
# This function is in parent class.
# This function is in child 1.
# This function is in parent class.
# This function is in child 2.



# Hybrid Inheritance:
# Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

# Example
class School:
    def func1(self):
        print("This function is in school.")
 
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
 
 
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
 
object = Student3()
object.func1()
object.func2()
Output:
# This function is in school.
# This function is in student 1.















# Access Specifiers/Modifiers
# Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

# Public Access Specifier in Python
# All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.

Example:
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"Harry")
print(obj.age)
print(obj.name)
# Output:
# 21
# Harry



# Private Access Modifier
# By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.

# In Python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.

# Example:
class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        
        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Harry")
obj1 = Subject

# calling by object of class Student
print(obj.__age)
print(obj.__funName())

# calling by object  of class Subject
print(obj1.__age)
print(obj1.__funName())
# Output:
# AttributeError: 'student' object has no attribute '__age'
# AttributeError: 'student' object has no method '__funName()'
# AttributeError: 'subject' object has no attribute '__age'
# AttributeError: 'student' object has no method '__funName()'
# Private members of a class cannot be accessed or inherited outside of class. If we try to access or to inherit the properties of private members to child class (derived class). Then it will show the error.

# Name mangling
# Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.

class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute







# Protected Access Modifier
# In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.

# It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.

# Example:
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName()) 
# Output:
# Harry
# CodeWithHarry

# Harry
# CodeWithHarry