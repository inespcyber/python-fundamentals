"""
Title:
Basic Password Strength Checker

Objective:
Ask the user to enter a password and verify if it meets basic security requirements.

Concepts Practised:
- User input
- For loops
- Conditional statements (if / else)
- Boolean variables
- String methods (isdigit)
- String length validation (len)

Note:
This script is created for educational purposes to practise Python fundamentals
and introduce basic security-related logic.
"""
# Ask the user to input a password
password = input("Enter your password: ")

# Initialize a boolean variable to track if the password contains a number
has_number = False

# Check each character in the password to see if it is a digit
for character in password:
    if character.isdigit():
        has_number = True

# Validate the password based on length and presence of a number
if len(password) >= 8 and has_number:
    print("Acceptable Password")
else:
    print("Weak Password")
