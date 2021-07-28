with open("guest.txt", "r") as f_obj:
    contents = f_obj.read()
    print(contents.strip())
    for line in contents:
        print(line.strip())

with open("guest.txt", "r") as f_obj:       
    contents_lines = f_obj.readlines()
    print(contents_lines)
    for line in contents_lines:
        print(line.strip())