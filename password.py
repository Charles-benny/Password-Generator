import random
import string

def generate_password(username, length=12):
    if length < 8 or length > 15:
        raise ValueError("Password length 8 - 15 characters")

    special_characters = "@#$%^*&!~"
    all_characters = string.ascii_letters + string.digits + special_characters
    
    while True:
        password = []
        password.append(random.choice(string.digits))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(special_characters))
        password.extend(random.choice(all_characters)
                        for _ in range(length - len(password)))
        random.shuffle(password)
        password_str = ''.join(password)
        if (len(set(password_str)) >= 4 and
            not any(char in username for char in password_str)):
            break
    
    return password_str

def main():
    print("Welcome to the Password Generator")

    username = input("Enter your username: ").strip()
    
    try:
        length = int(input("Enter the desired length of the password (8-15):  "))
    except ValueError:
        print("Invalid input. ")
        return
    
    try:
        password = generate_password(username, length)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
