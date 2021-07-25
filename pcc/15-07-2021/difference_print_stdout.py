# print("99") is equivalent to 

# import sys
# sys.stdout.write(str(99) + "\n")

lala = input("Sing something for me... ")

import sys
from time import sleep

for i in range(1, 10):
    sleep(0.1)
    sys.stdout.write(str(lala) + "  ")
    sys.stdout.flush()

thanks = "\n\nI love that tune. Thank you..."

for char in thanks:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
