"""
Title: 
BMI Calculator

Objective:
Ask the user for weight (kg) and height (m), calculate the Body Mass Index (BMI), and classify it.

Concepts Practised:
- User input
- Type conversion to float
- Arithmetic operations
- Conditional statements
- Printing formatted output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Ask the user for weight and height
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
# Calculate BMI
bmi = weight / (height * height)
# Print BMI with one decimal point
print(f"BMI: {bmi:.1f}")
# Classify BMI according to standard ranges and print the classification
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obesity Grade I")
else:
    print("Obesity Grade II or higher")
