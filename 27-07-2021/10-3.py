active = True
filename = "guest.txt"
while active == True:
    message = input("Please enter guest name. enter 'quit' to exit. ")
    if message == "quit":
        active = False
        break
    print("Thank you, " + message)
    with open(filename, "a") as file_object:
        file_object.write(message + "\n")


