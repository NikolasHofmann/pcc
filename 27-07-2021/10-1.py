with open("learning_python.txt") as file_object:
    contents = file_object.read()
    for i in range(0, 3):
        print(contents)
        i += 1

print("\n\n\n")

with open("learning_python.txt") as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.strip())

print("\n\n\n")

with open("learning_python.txt") as file_object:
    for line in file_object:
        print(line.strip())

print("\n\n\n")

with open("learning_python.txt") as file_object:
    lines = file_object.readlines()
    for line in lines:
        lala = line.replace("python", "c")
        print(lala.strip())

filename = "lala.txt"

with open(filename, "w") as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename, "a") as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")