# In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.
name = "Harry"
print("Hello, " + name)

# Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

# Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.

# How will you print this statement in python?: He said, "I want to eat an apple". We will definitely use single quotes for our convenience

sentence = 'He said, "I want to eat an apple".'
print(sentence)

#Multiline Strings
#If our string has multiple lines, we can create them like this:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Accessing Characters of a String In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0. Square brackets can be used to access elements of the string.
name = "Harry"
print(name[0])  # Output: H
print(name[1])  # Output: a
print(name[2])  # Output: r
print(name[3])  # Output: r
print(name[4])  # Output: y

# Looping through the string
# We can loop through strings using a for loop like this:

for character in name:
    print(character)






#7)String Slicing & Operations on String

# Length of a String
# We can find the length of a string using len() function.

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

# String as an array A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.
fruit = "Mango"
print(fruit[0])  # Output: M    
print(fruit[1])  # Output: a    
print(fruit[2])  # Output: n

# Slicing Example:
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index

#assesment question
nm="Aryan"
print(nm[-4:-2])