import re


def is_strong_password(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        raise ValueError("Password must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter.")
    if not re.search(r"\d", password):
        raise ValueError("Password must contain at least one digit.")
    if not re.search(r"[!@#$%^&*]", password):
        raise ValueError("Password must contain at least one special character (!@#$%^&*).")
    return True


def check_passwords(input_file="passwords.txt", output_file="strong_passwords.txt"):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                password = line.strip()
                if not password:
                    continue
                try:
                    if is_strong_password(password):
                        outfile.write(password + '\n')
                except ValueError as ve:
                    print(f"Password '{password}' is invalid: {ve}")

        print(f"Password check complete. Strong passwords saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    check_passwords()
