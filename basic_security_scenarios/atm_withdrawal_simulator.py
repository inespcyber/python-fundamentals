"""
Title: 
ATM Withdrawal Simulator

Objective:
Simulate an ATM withdrawal, checking for sufficient balance, positive amount, and multiples of 10.

Concepts Practised:
- User input
- Type conversion to float
- Conditional statements
- Arithmetic operations
- Printing output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Set initial account balance
balance = 2500.0

# Ask the user for withdrawal amount
withdrawal = float(input("Enter the amount you want to withdraw (multiples of 10 only): "))

# Validate withdrawal conditions
if withdrawal <= 0:
    print("The withdrawal amount must be positive.")
elif withdrawal > balance:
    print("Insufficient balance.")
elif withdrawal % 10 != 0:
    print("The withdrawal amount must be a multiple of 10.")
else:
    balance = balance - withdrawal
    print("Withdrawal successful!")
    print(f"Remaining balance: €{balance}")
