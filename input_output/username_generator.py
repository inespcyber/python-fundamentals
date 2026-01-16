"""
Title: 
Username Generator

Objective:
Ask the user for first name, last name, and birth year, then create a lowercase username.

Concepts Practised:
- User input
- String manipulation (lowercase, concatenation)
- Printing output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Ask for user details
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = input("Enter your birth year: ")

# Concatenate first name, last name, and year in lowercase to form username
username = first_name.lower() + "." + last_name.lower() + birth_year

# Print the generated username
print(f"Your username is {username}")
