# For Loop
# for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

name = 'Abhishek'
for i in name:
    print(i, end=", ")

colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)


# range():
# What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

# Here, we can use the range() function.

for k in range(5):
    print(k)


for k in range(4,9):
    print(k)



# While Loop
# As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

count = 5
while (count > 0):
  print(count)
  count = count - 1

  # Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the counter variable (the variable count, in our case) or the loop will continue forever.


# Else with While Loop
# We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.

x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')


# break statement
# The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

for i in range(12):
  print(" 5 X",i,"=",5*i)
  if(i==8):
      break
 

# continue statement
# The continue statement is used to skip the current block of code and move to the next iteration

for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)