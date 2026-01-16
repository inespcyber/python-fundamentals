"""
Title: 
Basic Access Control

Objective:
Ask for a username and grant access if the user is "admin" or "supervisor".

Concepts Practised:
- User input
- Conditional statements
- Logical OR operator
- Printing output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Ask the user to enter a username
user = input("Enter the username: ")
# Check if the username is "admin" or "supervisor" and print the result
if user == "admin" or user == "supervisor":
    print("Access granted.")
else:
    print("Access denied.")
