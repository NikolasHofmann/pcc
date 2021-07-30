import json

filename = "username.txt"

def load_username():
    try:
        with open(filename, "r") as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def new_username():
    username = input("What is the username? ")
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
        print("Updated the user name to " + username)
        return username

def get_username():
    if load_username():
        # confirm if it is the right user
        username = load_username()
        active = True
        while active:
            confirm = input("Is " + username + " the right username?(y/n)")
            if confirm == "y":
                active = False
                print("Welcome, " + username)
            elif confirm == "n":
                active = False
                new_username()
            else:
                print("Please enter y or n.")
                continue
    else:
        username = new_username()
        print("Stored " + username + ".")

get_username()


