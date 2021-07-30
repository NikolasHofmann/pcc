import sys
from termcolor import colored, cprint
from random import randint

primes = []
i = int
def is_prime(number):
    if number == 1:
        return True
    elif number == 2:
        return True
    elif number == 3:
        return True
    else:    
        for i in range(2, number):
            if number % i == 0:
                # not a prime number
                continue
            else:
                # is prime number
                return True


i = 3
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
