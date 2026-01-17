"""
Title:
Login Attempt Limitation System

Objective:
Simulate a login system that limits the number of authentication attempts
and blocks access after a defined number of failures.

Concepts Practised:
- User input
- While loops
- Conditional statements (if / else)
- Counters
- Boolean logic
- Break statements

Note:
This script is created for educational purposes to practise Python fundamentals
and introduce basic security concepts such as brute force protection.
"""
# Predefined correct password
password = "secret123"

# Maximum number of login attempts
attempts = 3

# Loop until the user runs out of attempts
while attempts > 0:
    typed_password = input("Enter your password: ")

    if typed_password == password:
        print("Access granted.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Wrong password. Try again.")
        else:
            print("Account blocked.")
