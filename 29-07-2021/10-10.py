with open("text.txt", "r") as file_object:
    lines = file_object.readlines()
    nonewline = []
    for line in lines:
        if not line == "\n":
            nonewline.append(line)

with open("nonewline.txt", "w") as file_object:
    for line in nonewline:
        if len(line) > 50:
            while len(line) > 50:
                fifty = line[:50] + "\n"
                file_object.write(fifty)
                line = line[50:]
            if line:
                file_object.write(line)
        else:
            file_object.write(line)

with open("text.txt", "r") as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line)