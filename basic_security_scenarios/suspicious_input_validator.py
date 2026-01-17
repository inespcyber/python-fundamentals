"""
Title:
Suspicious Input Detection

Objective:
Validate user input and detect potentially malicious patterns
commonly associated with SQL injection attempts (;, --, DROP).

Concepts Practised:
- User input
- String comparison
- Conditional statements (if / else)
- Logical operators
- Basic input validation
- Case-insensitive string handling

Note:
This script is created for educational purposes to practise Python fundamentals
and introduce defensive programming concepts to prevent common security issues.
"""
# Ask the user to input a message
user_input = input("Enter your message: ")

# Check for suspicious patterns in the input
if ";" in user_input or "--" in user_input or "DROP" in user_input.upper():
    print("Suspicious input detected.")
else:
    print("Input accepted.")
