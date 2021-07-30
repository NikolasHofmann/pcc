import json

def get_stored_number():
    filename = "favorite_number.txt"
    try:
        with open(filename, "r") as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def get_new_number():
    favorite_number = input("What is your favorite number? ")
    with open("favorite_number.txt", "w") as f_obj:
        json.dump(favorite_number, f_obj)
        return favorite_number

def get_favorite_number():
    favorite_number = get_stored_number()
    if favorite_number:
        print("Your number is " + favorite_number)
    else:
        favorite_number = get_new_number()
        print("Will store the following number: " + favorite_number)

get_favorite_number()