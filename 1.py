import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the password length: "))
        if length < 8:
            print("Password length should be at least 8 characters.")
            return
        password = generate_random_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
