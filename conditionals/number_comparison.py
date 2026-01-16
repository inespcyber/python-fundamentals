"""
Title: 
Number Comparison

Objective:
Ask the user for two numbers and determine which one is greater or if they are equal.

Concepts Practised:
- User input
- Type conversion to float
- Conditional statements (if / elif / else)
- Printing output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Ask the user for two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Compare both numbers to determine the greater one or equality and print the result
if number1 > number2:
    print("The first number is greater.")
elif number2 > number1:
    print("The second number is greater.")
else:
    print("Both numbers are equal.")
