"""
Title: 
Loan Approval System

Objective:
Evaluate a loan request based on income, age, and credit history according to predefined rules.

Concepts Practised:
- User input
- Type conversion to float/int
- Conditional statements
- Logical AND / OR operators
- Printing output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Ask the user for monthly income, age, and credit history
income = float(input("Enter monthly income: "))
age = int(input("Enter age: "))
credit_history = input("Credit history (good/bad): ")

# Evaluate loan approval conditions and print the result
if income >= 5000 and credit_history == "good":
    print("Loan approved.")
elif 3000 <= income < 5000 and credit_history == "good" and age > 30:
    print("Loan approved.")
elif income > 8000 and credit_history == "bad" and age > 40:
    print("Loan goes for manual review.")
else:
    print("Loan denied.")
