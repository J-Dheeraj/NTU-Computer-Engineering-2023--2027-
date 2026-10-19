# Existing users in the system
existing_users = {
    'Test': 'Test12345',
    'Jack': 'Test12345',
    'Tom': 'Password1'
}

def is_strong_password(password):
    # Check the password strength criteria
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

def is_username_taken(username):
    # Check if the username already exists in the system
    return username in existing_users

def register_user(username, password):
    if is_username_taken(username):
        print("The user exists. Please choose another user name.")
    else:
        if is_strong_password(password):
            existing_users[username] = password
            print("User registered.")
        else:
            print("Your password is weak. Please enter a new password")

# User registration
print("User registration:")
while True:
    user_name = input("Input your user name: ")
    if not is_username_taken(user_name):
        break

while True:
    user_password = input("Input your password:\n1. the password has at least one upper case letter\n2. the password has at least one lower case letter\n3. the password has at least one digit\n4. its length is more than 8\n")
    if is_strong_password(user_password):
        register_user(user_name, user_password)
        break

# Display the users in the system
print("The users in the system")
print(existing_users)
