import random
import string


def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choices(all_chars, k=length))

    return password


def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    print(f"Your generated password is: {password}")


if __name__ == "__main__":
    main()


   
