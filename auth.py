def check_auth():
    username = input("Enter username: ")
    if username == "Akash":
        password = input("Enter password: ")
        if password == "Hello":
            print("Login success")
        else:
            print("Password is incorrect.")
    else:
        print("Invalid username.")

check_auth()