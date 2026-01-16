"""
Title: 
Theme Park Ticket System

Objective:
Calculate ticket price based on visitor age and optional fast-pass.

Concepts Practised:
- User input
- Type conversion to integer
- Conditional statements
- Logical operators
- Arithmetic operations
- Printing output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Ask for visitor age and Fast-Pass option
age = int(input("Enter the visitor's age: "))
fast_pass = input("Do you want the Fast Pass? (yes/no): ")

# Determine ticket price based on age and Fast-Pass option
price = 0

# Calculate base price
if age < 3:
    price = 0
    print("Free entry for children under 3.")
elif 3 <= age <= 12:
    price = 15
elif 13 <= age <= 17:
    price = 25
elif 18 <= age <= 59:
    price = 40
else:
    price = 20

# Add Fast-Pass cost if applicable
if age >= 3 and fast_pass == "yes":
    price += 30

# Print final ticket price
print(f"Final ticket price: €{price:.2f}")
