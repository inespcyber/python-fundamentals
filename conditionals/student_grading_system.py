"""
Title: 
Student Grading System

Objective:
Ask the user for a student grade (0–10) and provide a status: Approved, Recovery, or Failed. Validate input.

Concepts Practised:
- User input
- Type conversion to float
- Conditional statements
- Input validation
- Printing output

Note:
This script is created for educational purposes to practise Python fundamentals.
"""
# Ask the user to enter the student's grade
grade = float(input("Enter the student's grade (0 to 10): "))

# Determine status based on grade and print the result
if grade < 0 or grade > 10:
    print("Invalid grade.")
elif grade >= 7: 
    print("Approved")
elif grade >= 5:
    print("Recovery")
else:
    print("Failed")
