#Shane Hylton, Michael Ippolito, Nate Aiken

#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.
test1 = float(input('Enter the score for test 1: '))
test2 = float(input('Enter the score for test 2: '))
test3 = float(input('Enter the score for test 3: '))
# Converted values to floats and added test3
# Calculate the average test score.
average = (test1 + test2 + test3 )/ 3
#added parentheses around test scores
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!')

#indented the second print statement

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
l1 = float(input("Enter the length of the first rectangle: "))
w1 = float(input("Enter the width of the first rectangle: "))
l2 = float(input("Enter the length of the second rectangle: "))
w2 = float(input("Enter the width of the second rectangle: "))

#added floating point inputs for each dimension
a1 = l1*w1
a2 = l2*w2

#computed areas

print("Area 1: ", a1)
print("Area 2: ", a2)

#printed areas
#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

name = str(input("Enter your first name: "))
age = int(float(input("Enter your age: ")))

# Assuming that the user is cooperative and enters an int or a float

#nested input statements inside of str(), int()

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

print(f"Happy birthday {name}! You are {age} years old today!")
#Used an f-string to print both string text and variables

print("Happy birthday", name, "You are", age, "Years old today!")

#alternative solution to print statement

