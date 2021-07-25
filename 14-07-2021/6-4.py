tastyness = {
    "pizza": 5,
    "döner": 5,
    "burger": 5,
    "salad": 2,
    "pizza": 6
}

print(tastyness)

# makes a string list of the values

list_value = []
for value in tastyness.values():
    list_value.append(str(value))

print(list_value)


# converts the values to strings

for value, key in tastyness.items():
    tastyness[value] = str(key)

print(tastyness)

print(set(tastyness.keys()))
print(set(tastyness.values()))


print(sorted(tastyness.keys()))
print(tastyness.keys())

print(tastyness.values())
print(sorted(tastyness.values()))

# # # # # # 6-4 # # # # # #

words = {
    "dictionary": "The dictionary is like a list of keys, each key pointing "
    "to a specific value.",
    "indentation": "The amount of spaces before code.",
    "increment": "Die Erhöhung.",
    "elif": "Else if..."
}

for key, value in words.items():
    print("Key: " + key +" \nValue: " + value + "\n")

# # # # # # 6-5 # # # # # #

rivers = {
    "nile": "egypt",
    "thames": "england",
    "moldau": "russia"
}

for key, value in rivers.items():
    print("The " + key.title() + " runs through " + value.title())

for key in rivers.keys():
    print(key.title())

for value in rivers.values():
    print(value.title())


# # # # # # 6-6 # # # # # # 

favorite_languages = {
    "nikolas": "python",
    "lilli": "bayrisch",
    "mirco": "deutsch"
}

new_people = {
    "julia": "deutsch",
    "gabriel": "türkisch",
    "nikolas": "python",
    "lilli": "bayrisch"
}

for person in new_people.keys():
    if person in favorite_languages.keys():
        print("\nThank you for participating in the poll, " + person + ".\n")
    else:
            print("\nPlease take the poll, " + person + ".\n")


for number in range(30):
    print(number)

# # # # # # 6-7 # # # # # #

person0 = {
    "first_name": "Mirco", 
    "last_name": "Engelhard", 
    "age": "32", 
    "city": "Köln"
}

person1 = {
    "first_name": "Konrad",
    "last_name": "Graf",
    "age": "32",
    "city": "Hamburg"
}

person2 = {
    "first_name": "Levin",
    "last_name": "Melches",
    "age": "32",
    "city": "Köln"
}

people = [person0, person1, person2]

for person in people:
    for key, value in person.items():
        print(key + ": " + value)
    print()

# # # # # # 6-8 # # # # # # 

kitty = {
    "animal_kind": "cat",
    "owner_name": "charles"
}

fishy = {
    "animal_kind": "fish",
    "owner_name": "cool george"
}

casper = {
    "animal_kind": "horse",
    "owner_name": "jim"
}

shiggy = {
    "animal_kind": "turtle",
    "owner_name": "fred"
}

pets = [kitty, fishy, casper, shiggy]

print(pets)

for pet in pets:
    for key, value in pet.items():
        print(key + ": " + value.title())
    
    print("\n")


# # # # # # 6-9 # # # # # # 

favorite_places = {
    "bernhard": ["barcelona", "brussels", "gran canaria"],
    "mirco": ["medellin", "köln"],
    "nikolas": ["barcelona"]
}

for key, value in favorite_places.items():
    places = []
    for place in value:
        places.append(place.title())

    if len(places) > 1:
        print(key.title() + "'s favorite places are: ")
    else:
        print(key.title() + "'s favorite place is: ")

    print(*places, sep = ", ")
    print("\n")


# nested lists and dictionary within a dictionary
favorite_numbers = {
    "mirco": ["5", "1"],
    "dennis": ["2", "0"],
    "damien": ["8", "3"],
    "lilli": {
        "7": ["1", "2", "3"],
        "5": ["9", "8", "7"]
    }
}

print(favorite_numbers)
print(favorite_numbers["mirco"])
print("\n\n")
print(favorite_numbers["lilli"]["7"][0])

lillis_numbers = []
for key, value in favorite_numbers["lilli"].items():
    for number in value:
        lillis_numbers.append(number)

for number in lillis_numbers:
    print(*number, sep = ", ")

print(lillis_numbers)
    