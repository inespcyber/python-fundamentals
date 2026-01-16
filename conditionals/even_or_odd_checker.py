"""
Title: 
Even or Odd Number Checker

Objective:
Ask the user for an integer and determine whether it is even or odd.

Concepts Practised:
- User input
- Type conversion to integer
- Conditional statements (if / else)
- Modulo operator
- Printing output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Ask the user to enter an integer
number = int(input("Enter an integer: "))

# Check if the number is even or odd and print the result
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
