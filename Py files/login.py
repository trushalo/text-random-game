'''CREATE USER AND LOGIN PROCESS'''

'''import hashlib

def create_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hash the password for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Write user information to a file
    with open("users.txt", "a") as f:
        f.write(f"{username}:{hashed_password}\n")

    print("User created successfully!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open("users.txt", "r") as f:
        for line in f:
            user, stored_password = line.strip().split(":")
            if user == username and stored_password == hashed_password:
                print("Login successful!")
                return
        print("Invalid username or password.")

# Main program
while True:
    print("1. Create User")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_user()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
'''