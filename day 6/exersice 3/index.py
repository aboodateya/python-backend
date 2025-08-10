class InvalidLengthError(Exception):
    """Raised when the username length is not between 5 and 15 characters."""
    pass

class InvalidCharacterError(Exception):
    """Raised when the username contains non-alphanumeric characters."""
    pass


def validate_username(username):
    if not (5 <= len(username) <= 15):
        raise InvalidLengthError("Username must be between 5 and 15 characters long.")
    if not username.isalnum():
        raise InvalidCharacterError("Username must contain only alphanumeric characters.")


def register_user():
    username = input("Enter a username: ").strip()
    success = False

    try:
        validate_username(username)


        with open("users.txt", "a") as file:
            file.write(username + '\n')
        
        print(f"User '{username}' registered successfully.")
        success = True

    except InvalidLengthError as ile:
        print(f"Invalid Length Error: {ile}")
    except InvalidCharacterError as ice:
        print(f"Invalid Character Error: {ice}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Registration attempt completed.")
        print("Status:", "Success ✅" if success else "Failed ❌")



if __name__ == "__main__":
    register_user()
