"""
Title: 
Discount Calculator

Objective:
Calculate a discount based on purchase amount and VIP status.

Concepts Practised:
- User input
- Type conversion to float
- Conditional statements
- Logical AND / OR operators
- Printing formatted output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Ask the user for purchase amount and VIP status
purchase = float(input("Enter the purchase value: "))
vip = input("Is the customer VIP? (yes/no): ")

# Determine discount based on purchase amount and VIP status
if purchase > 500 and vip == "yes":
    discount = 0.15
elif purchase > 500 or vip == "yes":
    discount = 0.10
else:
    discount = 0
  
# Calculate total after discount
total = purchase * (1 - discount)

# Print discount and total amount to pay
print(f"Discount applied: {discount * 100:.0f}%")
print(f"Final amount to pay: {total:.2f}€")
