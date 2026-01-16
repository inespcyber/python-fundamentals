"""
Title: 
Age Verification

Objective:
Ask the user for their age and determine if they are legally an adult (18 years or older).

Concepts Practised:
- User input
- Type conversion to integer
- Conditional statements (if / else)
- Printing output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Ask the user to enter their age
age = int(input("Enter your age: "))
# Check if the user is an adult or a minor and print the result
if age >= 18:
    print("You are of legal age.")
else:
    print("You are a minor.")
