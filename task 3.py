import re

def check_password_complexity(password):
    # Define criteria
    length_criteria = 8
    uppercase_criteria = 1
    lowercase_criteria = 1
    digit_criteria = 1
    special_char_criteria = 1
    special_chars = r"[!@#$%^&*()\-_=+\\|`~{}\[\]:;\"'<>,.?/]"

    # Check length
    if len(password) < length_criteria:
        return False, "Password should be at least {} characters long".format(length_criteria)
    # Check uppercase
    if not any(char.isupper() for char in password):
        return False, "Password should contain at least one uppercase letter"

    # Check lowercase
    if not any(char.islower() for char in password):
        return False, "Password should contain at least one lowercase letter"

    # Check digit
    if not any(char.isdigit() for char in password):
        return False, "Password should contain at least one digit"

    # Check special characters
    if not re.search(special_chars, password):
        return False, "Password should contain at least one special character"

    return True, "Password meets complexity criteria"

# Test the function
password = input("Enter your password: ")
valid, message = check_password_complexity(password)
print(message)
