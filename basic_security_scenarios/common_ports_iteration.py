"""
Title: 
Common Ports Iteration

Objective:
Iterate over a list of common network ports and print a message for each, simulating a basic port check.

Concepts Practised:
- For loops
- Iterating over a list
- Printing output
- Basic cybersecurity context (ports)

Note:
This script is created for educational purposes to practise Python fundamentals and basic security concepts.
"""
# Define a list of common ports
common_ports = [21, 22, 80, 443, 8080]

# Iterate over the list and print each port being checked
for port in common_ports:
    print(f"Checking port: {port}")
