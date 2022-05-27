def check_username():
    username = input("Enter username: ")
    if username == "Akash":
        return True
        
def check_password():
    password = input("Enter password: ")
    if password == "Hello":
        return True

if check_username() and check_password():
    print("Login success.")
else:
    print("Username or password is incorrect.")
