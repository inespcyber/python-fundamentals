"""
Title: 
Number Guessing Game

Objective:
Have the user guess a predefined secret number and give feedback: correct, too high, or too low.

Concepts Practised:
- User input
- Type conversion to integer
- Conditional statements
- Comparison operators
- Printing output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Set the predefined secret number
secret_number = 22

# Ask the user to guess the number
guess = int(input("Guess the secret number: "))

# Compare the guess with the secret number and print the result
if guess == secret_number:
    print("Correct!")
elif guess > secret_number:
    print("Too high.")
else:
    print("Too low.")
