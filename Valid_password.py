import re

# Function to check if a password is valid
def is_valid_password(password):
    # Check the length of the password
    if not 6 <= len(password) <= 12:
        return False
    # Check if the password matches all the criteria using regular expressions
    return bool(re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])", password))

# Accept input from the user as a single line of passwords separated by spaces
passwords = input("Enter passwords separated by spaces: ").split()

# Initialize a list to store valid passwords
valid_passwords = []

# Iterate through the passwords and check their validity
for password in passwords:
    if is_valid_password(password):
        valid_passwords.append(password)

# Print the valid passwords separated by newlines
print("\n".join(valid_passwords))