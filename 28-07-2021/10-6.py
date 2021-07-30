active = True

while active:    
    first_number = input("Please enter the first number. Type 'quit' to quit. ")
    if first_number == "quit":
            active = False
            break
    second_number = input("Please enter the second number. Type 'quit' to quit. ")
    if second_number == "quit":
            active = False
            break

    a = 0
    b = 0
    condition1 = False
    condition2 = False

    try:
        int(first_number)
    except: 
        print("First input is not a number...")
    else:
        a = int(first_number)
        condition1 = True

    try:
        int(second_number)
    except:
        print("Second input is not a number...")
    else:
        b = int(second_number)
        condition2 = True

    final_number = a + b

    if not condition1 and not condition2:
        print("None of the inputs are numbers...")
    else:
        print(final_number)

