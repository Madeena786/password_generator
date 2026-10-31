import secrets
import string
def generate_password(length, use_letters, use_numbers, use_symbols):
    characters=""
    if use_letters:
        characters+=string.ascii_letters
    if use_numbers:
        characters+=string.digits
    if use_symbols:
        characters+= string.punctuation
    if characters=="":
        return None
    password=""
    for i in range(length):
        password+=secrets.choice(characters)
    return password
print("===================================")
print("       PASSWORD GENERATOR")
print("===================================")
length=int(input("Enter password length: "))
letters=input("Include letters? (yes/no): ").lower()
numbers=input("Include numbers? (yes/no): ").lower()
symbols=input("Include symbols? (yes/no): ").lower()
use_letters=letters=="yes"
use_numbers=numbers=="yes"
use_symbols=symbols=="yes"
if length<=0:
    print("Password length must be greater than 0.")
else:
    password=generate_password(
        length,
        use_letters,
        use_numbers,
        use_symbols
    )
    if password is None:
        print("Please select at least one character type.")
    else:
        print()
        print("Generated Password:", password)
        print("Password Length:", len(password))
