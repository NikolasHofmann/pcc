with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    if contents == "3.1415926535\n8979323846\n2643383279":
        print("yes")


filename = "pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line)

print("\n\n\n")

filename = "pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.rstrip()

print(pi_string)