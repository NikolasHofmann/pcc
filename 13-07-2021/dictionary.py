alien_0 = {"color": "green"}
print(alien_0["color"])

alien_0 = {5: "blue"}
print(alien_0[5])

alien_0 = {5: 6}
print(alien_0[5])

alien_0 = {"color": "green", "points": 5}
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

lala = ["hello", "dog", "cat",5]
print(lala)

dictionary = {}
dictionary["word1"] = "hello"
print(dictionary["word1"])

dictionary["word2"] = "dog"
print(dictionary["word1"]+" "+dictionary["word2"])

############ alien moving ############

alien_0 = {"x_position": 0, "y-position": 25, "speed": "medium"}
print("Original x-position: " + str(alien_0["x_position"]))
print("Original y-position: " + str(alien_0["y-position"]))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # this must be a fast alien...
    x_increment = 3

# The new position is the old position plus the increment.
alien_0["x_position"] = alien_0["x_position"] + x_increment

print("New x-position: " + str(alien_0["x_position"]))

del alien_0["speed"]
print(alien_0)

favorite_languages = {
    "nikolas": "python",
    "lilli": "bayrisch",
    "mirco": "deutsch",
}

print(favorite_languages["nikolas"])
print(favorite_languages)

# loop through dictionary
person = {
    "first_name": "Mirco", 
    "last_name": "Engelhard", 
    "age": "32", 
    "city": "Köln"
}
print(person)

for key, value in person.items():
    print("\nKey: " + key)
    print("Value: " + value)

for value in person.values():
    print(value.upper())

for key in person.keys():
    print(key.title())


print(favorite_languages)

friends = ["lilli", "nikolas"]
print(favorite_languages.keys())
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", your favorite language is " +
            favorite_languages[name].title() + ".")




