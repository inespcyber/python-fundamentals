"""
Title: 
Game Access Validation

Objective:
Determine if a player can join a game based on level and restriction list status.

Concepts Practised:
- User input
- Type conversion to integer
- Conditional statements
- Logical AND operator
- Printing output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Ask the user to enter the player's level and restriction status
level = int(input("Enter the player's level: "))
restriction = input("Is the player on the restriction list? (yes/no): ")

# Check access conditions and print the result
if level >= 10 and restriction == "no":
    print("Access allowed.")
else:
    print("Access not allowed.")
