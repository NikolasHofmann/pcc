import sys
from termcolor import colored, cprint
from random import randint

i = 2
while True:
    do = input()
    if do == "q":
        break
    else:
        i_string = str(i)
        # print("i = " + i_string)
        random_number = randint(1, len(i_string))
        # print("The random number is " + str(random_number))
        # print("output from start to random number: " + i_string[:random_number])
        output = i_string[:random_number]
        # print("output from random number to end: " + i_string[random_number:])
        output += "__here__" + i_string[random_number:]
        print(colored(output, "red"))
        
        i = i**2
