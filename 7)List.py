# 14)List
# -Lists are ordered collection of data items.
# -They store multiple items in a single variable.
# -List items are separated by commas and enclosed within square brackets [].
# -Lists are changeable meaning we can alter them after creation.

lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)

details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)


# Positive Indexing:
# As we have seen that list items have index, as such we can access items using these indexes.

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])


# Negative Indexing:
# Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])


# Check whether an item in present in the list?
# We can check if a given item is present in the list. This is done using the in keyword.

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Orange" in colors:
    print("Orange is present.")
else:
    print("Orange is absent.")


# Range of Index:
# You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'


# printing all element from a given index till the end
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes


# printing all elements from start to a given index
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes


# Printing alternate values
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes


# printing every 3rd consecutive value withing a given range
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])



# List Comprehension

# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
# List = [Expression(item) for item in iterable if Condition]
# Expression: It is the item which is being iterated.
# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
# Condition: Condition checks if the item should be added to the new list or not


# Example 1: Accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

# Example 2: Accepts items with the small letter “a” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_A = [item for item in names if "a" in item]
print(namesWith_A)








# List Methods

#list.sort() This method sorts the list in ascending order. The original list is updated
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

# What if you want to print the list in descending order?
# We must give reverse=True as a parameter in the sort method.
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)


# reverse() This method reverses the order of the list.
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)


# ndex() This method returns the index of the first occurrence of the list item.
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))


# count() Returns the count of the number of items with the given value.\
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))    

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(2))


# copy() Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
colors = ["voilet", "green", "indigo", "blue", "green"]
new_colors = colors.copy()
print(new_colors)


# append(): This method appends items to the end of the existing list.
colors = ["voilet", "green", "indigo", "blue", "green"]
colors.append("yellow")
print(colors)


# insert(): This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
colors = ["voilet", "green", "indigo", "blue", "green"]
colors.insert(2, "yellow")
print(colors)


# extend(): This method adds the specified list elements (or any iterable) to the end of the current list. The original list is updated.
colors = ["voilet", "green", "indigo", "blue", "green"] 
new_colors = ["yellow", "orange", "red"]
colors.extend(new_colors)
print(colors)


# Concatenating two lists: You can simply concatenate two lists to join two lists.
colors = ["voilet", "green", "indigo", "blue", "green"]
new_colors = ["yellow", "orange", "red"]
all_colors = colors + new_colors
print(all_colors)