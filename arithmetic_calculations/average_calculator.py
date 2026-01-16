"""
Title: 
Average Calculator

Objective:
Ask the user to enter three decimal numbers and calculate their arithmetic average.

Concepts Practised:
- User input
- Type conversion to float
- Arithmetic operations
- Printing output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Ask the user to enter three decimal numbers
a = float(input("Enter a first number: "))
b = float(input("Enter a second number: "))
c = float(input("Enter a third number: "))
# Calculate the average
average=(a+b+c) / 3
# Print the result
print (f"The average of these 3 numbers is {average}")
