"""
Title: 
Rectangle Area and Perimeter Calculator

Objective:
Ask the user for the width and height of a rectangle, then calculate and display the area and perimeter.

Concepts Practised:
- User input
- Type conversion to float
- Arithmetic operations (area, perimeter)
- Printing output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Ask the user to enter rectangle dimensions
width = float(input("Enter the width of the rectangle in meters: "))
height = float(input("Enter the height of the rectangle in meters: "))
# Calculate area and perimeter
area = width * height
perimeter = 2 * (width + height)
# Print the results
print("Rectangle area:", area, "m²")
print("Rectangle perimeter:", perimeter, "m")
