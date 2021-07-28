active = True

while active == True:
    message = input("Why do you like programming? Type 'quit' to quit. ")
    if message == "quit":
        print("Thank you. Bye.")
        break
    with open("reasons_list.txt", "a") as file_object:
        file_object.write(message + "\n")
