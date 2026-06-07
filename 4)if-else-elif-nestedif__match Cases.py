# i)if-else
# if the expression evaluates True: Execute the block of code inside if statement. After execution return to the code out of the if……else block.\
# if the expression evaluates False: Execute the block of code inside else statement. After execution return to the code out of the if……else block.

applePrice = int(input("Enter Price Of Apple: "))
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")


# ii)elif
# if the expression evaluates True: Execute the block of code inside if statement. After execution return
# to the code out of the if……elif……else block.\
# if the expression evaluates False: Evaluate the next condition in elif statement. If it is True, execute the block of code inside elif statement. After execution return to the code out of the if……elif……else block. If it is False, evaluate the next condition in elif statement and so on until there are no more elif statements left. If all conditions are False, execute the block of code inside else statement. After execution return to the code out of the if……elif……else block.

marks = int(input("Enter Your Marks: "))
if (marks >= 90):
    print("Grade: A")       
elif (marks >= 80):
    print("Grade: B")
elif (marks >= 70):
    print("Grade: C")
elif (marks >= 60):
    print("Grade: D")



# iii)Nested if statements
# We can use if, if-else, elif statements inside other if statements as well.
# it give condition in condition means in if or elif statement we have anothe condion if-else-elif

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")



# Excersice 2: Good Morning Sir
# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:

time=float(input("Enter Time: "))

if(time>=4 and time<12):
  print("Good Morning")

elif(time>=12 and time<17):
  print("Good Afternoon")

elif(time>=17 and time<21):
  print("Good Evening")



# 10) Match Case
# A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.
# The match case consists of three main entities :
# 1)The match keyword 2)One or more case clauses 3)Expression for each case
# The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.

day = input("Enter the day of the week: ")
match day:
    case "Monday":
        print("Today is Monday.")
    case "Tuesday":
        print("Today is Tuesday.")
    case "Wednesday":
        print("Today is Wednesday.")
    case "Thursday":
        print("Today is Thursday.")
    case "Friday":
        print("Today is Friday.")
    case "Saturday":
        print("Today is Saturday.")
    case "Sunday":
        print("Today is Sunday.")
    case _:
        print("Invalid day of the week.")