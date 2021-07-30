from termcolor import colored, cprint

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
        for i in range(2, number ):
            if number % i == 0:
                # not a prime number
                output = str(number) + " % " + str(i) + " is 0."
                print(colored(output, "green"))
                print(colored("it is not a prime number\n", "green"))
                return False
            else:
                # is prime number
                output = str(number) + " % " + str(i) + " is more than 0."
                print(colored(output,"red"))
                print(colored("it is a prime number\n" , "red"))
                continue

        return True         

for k in range(1,10000000):
    is_prime(k)



while True:
    tellme = input()
    if is_prime(int(tellme)):
        print(colored("it is a prime number\n" , "red"))
    else:
        print(colored("it is not a prime number\n", "green"))