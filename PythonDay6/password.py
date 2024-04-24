import re

def is_strong_password(password):
    # Define regex patterns for letters, numbers, and special characters
    letter_pattern = re.compile(r'[a-zA-Z]')
    number_pattern = re.compile(r'[0-9]')
    special_char_pattern = re.compile(r'[^a-zA-Z0-9]')

    # Check if the password contains at least one letter, one number, and one special character
    has_letter = bool(letter_pattern.search(password))
    has_number = bool(number_pattern.search(password))
    has_special_char = bool(special_char_pattern.search(password))

    # Check if all criteria are met
    if has_letter and has_number and has_special_char:
        return True
    else:
        return False

if __name__ == "__main__":
    password = input("Enter your password: ")
    if is_strong_password(password):
        print("Strong password!")
    else:
        print("Weak password! Password should contain letters, numbers, and special characters.")
