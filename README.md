# Password Manager 🔐

A simple command-line password manager that encrypts and stores your passwords securely using Python's `cryptography` library.

## Features
- Add new passwords for different accounts.
- View stored passwords with decryption.
- Secure encryption using the `Fernet` symmetric encryption algorithm.
- Easy-to-use interface.

## Prerequisites
- Python 3.x installed on your system.
- `cryptography` library. Install it using:

```bash
pip install cryptography

----
Usage

1.Clone the repository:
  git clone https://github.com/yourusername/password-manager.git
  cd password-manager

2.Generate a key (if running for the first time): Uncomment and run the write_key() function in the script to generate the encryption key:
  def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

3.Run the program:
  python password_manager.py

4.Choose an action:

  Type add to add a new password.
  Type view to view existing passwords.
  Type q to quit the program.

File Structure
1.password_manager.py: The main script for the password manager.
2.key.key: Stores the encryption key. Keep this file secure!
3.passwords.txt: Stores encrypted passwords. This file is created automatically.

Example

1.Adding a Password
  Would you like to add a new password or view existing ones (view, add), press q to quit? add
  Account Name: Gmail
  Password: mysecurepassword123
  Password added successfully.

2.Viewing Passwords
  Would you like to add a new password or view existing ones (view, add), press q to quit? view
  User: Gmail | Password: mysecurepassword123

Security Notes

  Do not share the key.key file with anyone. It is required to decrypt your stored passwords.
  Store the key.key file in a secure location, separate from passwords.txt.
  Use strong and unique passwords for your accounts.
