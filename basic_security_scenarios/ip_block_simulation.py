"""
Title:
IP Login Attempt Block Simulation

Objective:
Simulate a basic security mechanism that tracks failed login attempts
from a single IP address and blocks access after a defined limit is reached.

Concepts Practised:
- User input
- While loops
- Conditional statements (if / else)
- Counters and state tracking
- Boolean variables
- Break statements

Note:
This script is created for educational purposes to practise Python fundamentals
and introduce basic security concepts such as brute force mitigation and IP-based access blocking.
"""
# Get the IP address from the user
ip_address = input("Enter IP address: ")

# Predefined correct password
password = "secret123"

# Initialize failed attempts counter and block status
failed_attempts = 0
ip_blocked = False

# Loop until the IP is blocked or access is granted
while not ip_blocked:
    typed_password = input("Enter your password: ")

    if typed_password == password:
        print("Access granted.")
        break
    else:
        failed_attempts += 1
        print("Wrong password.")

        if failed_attempts >= 5:
            ip_blocked = True
            print(f"IP {ip_address} has been blocked due to too many failed login attempts.")
        else:
            print(f"Failed attempts: {failed_attempts}. Try again.")
