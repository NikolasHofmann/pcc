from collections import OrderedDict

words = OrderedDict()
words["dictionary"] = "The dictionary is like a list of keys, each key pointing "
words["indentation"] = "The amount of spaces before code."
words["increment"] = "Die Erhöhung..."

for key, value in words.items():
    print("Key: " + key + " Value: " + value)

print("\n")

# 9-14

from random import randint
x = randint(1, 10000000)
print(x)

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint (1, self.sides)
        print("The random number is: " + str(x))
    
    def change_die(self):
        self.sides = 10000000


aleya = Die()
aleya.roll_die()
print("changing dice...")
aleya.change_die()
aleya.roll_die()
print("\naleya100...")
aleya100 = Die(100)
aleya100.roll_die()