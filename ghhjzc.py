password = input("Enter a password: ")
if len(password) < 8:
    print("Password must have at least 8 characters.")
if not any(letter.isdigit() for letter in password):
    print("Password must contain a number.")
if not any(letter.isupper() for letter in password):
    print("Password must contain an uppercase letter.")
if "password" in password.lower():
    print("Password must not contain the word 'password'.")
if (  len(password) >= 8
    and any(letter.isdigit() for letter in password)
    and any(letter.isupper() for letter in password)
    and "password" not in password.lower)
    print("Password is valid.")Test cases and sample output

