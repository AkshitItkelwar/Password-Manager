from cryptography.fernet import Fernet
import os

# Generate and write a key to a file (uncomment to use initially)
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    """Loads the encryption key from the key.key file."""
    if not os.path.exists("key.key"):
        print("Key file not found. Please generate a key first.")
        exit()
    with open("key.key", "rb") as file:
        key = file.read()
    return key

def ensure_password_file():
    """Ensures the passwords.txt file exists."""
    if not os.path.exists("passwords.txt"):
        with open("passwords.txt", "w") as f:
            pass  # Create an empty file if it doesn't exist

def view():
    """View all stored passwords."""
    ensure_password_file()
    try:
        with open('passwords.txt', 'r') as f:
            lines = f.readlines()
            if not lines:
                print("No passwords saved yet.")
                return
            for line in lines:
                data = line.strip()
                if "|" in data:
                    user, passw = data.split("|")
                    try:
                        decrypted_password = fer.decrypt(passw.encode()).decode()
                        print(f"User: {user} | Password: {decrypted_password}")
                    except Exception as e:
                        print(f"Error decrypting password for {user}: {e}")
                else:
                    print(f"Invalid data format in file: {data}")
    except Exception as e:
        print(f"Error reading passwords file: {e}")

def add():
    """Add a new password."""
    name = input('Account Name: ').strip()
    pwd = input("Password: ").strip()

    if not name or not pwd:
        print("Account name and password cannot be empty.")
        return

    try:
        encrypted_password = fer.encrypt(pwd.encode()).decode()
        with open('passwords.txt', 'a') as f:
            f.write(f"{name}|{encrypted_password}\n")
        print("Password added successfully.")
    except Exception as e:
        print(f"Error adding password: {e}")

# Main Program
key = load_key()
fer = Fernet(key)

while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), or press q to quit? ").lower()
    if mode == "q":
        print("Exiting the program.")
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please choose 'view', 'add', or 'q'.")
