import random
import string

def generate_password(length=12):
    """
    Generate a random password with a specified length.

    Args:
        length (int): Length of the password.

    Returns:
        str: Random password.
    """
    # Define characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choice()
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    try:
        # Get user input for password length
        password_length = int(input("Enter the desired password length: "))

        # Generate password
        password = generate_password(password_length)

        # Display the generated password
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}")

