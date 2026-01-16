"""
Title: 
Triangle Classifier

Objective:
Ask the user for three side lengths and determine if a triangle is valid and its type.

Concepts Practised:
- User input
- Type conversion to float
- Conditional statements
- Logical operators
- Printing output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Ask the user for three side lengths
side1 = float(input("Enter the length of the first side of a triangle: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the sides can form a triangle and classify it
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        print("The triangle is Equilateral (all sides equal).")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is Isosceles (two sides equal).")
    else:
        print("The triangle is Scalene (all sides different).")
else:
    print("The given values cannot form a triangle.")
