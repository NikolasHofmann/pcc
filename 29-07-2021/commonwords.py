with open("nonewline.txt") as file_object:
    contents_lower = file_object.read().lower()
    count = contents_lower.count(".")
    print(count)