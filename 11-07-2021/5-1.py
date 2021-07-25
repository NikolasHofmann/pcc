notes = ["c","d","e","f"]

if "c" in notes:
    print("c is one of the notes...")

if "g" not in notes:
    print("g is not one of the notes...")

if notes[3] == "f":
    print("yes")

"a" <= notes[0]

car = "Audi"
car.lower() == "audi"
print("audi".upper())
"audi".title() == car

# 5-3 Alien colors

alien_color = "green"
if alien_color == "green":
    print("Congratulations, you earned 5 points!")

if alien_color != "blue":
    print("The color is not blue!")

alien_color = "green"
if alien_color == "green":
    print("The color is green.")
elif alien_color == "purple":
    print("The color is purple.")
else:
    print("Unknown color.")

alien_color = "purple"
if alien_color == "green":
    print("The color is green.")
elif alien_color == "purple":
    print("The color is purple.")
else:
    print("Unknown color.")

alien_color = "red"
if alien_color == "green":
    print("The color is green.")
elif alien_color == "purple":
    print("The color is purple.")
else:
    print("Unknown color.")


for age in range(0,100):
    if age < 2:
        print(str(age) + " Baby")
    elif age >= 2 and age < 4:
        print(str(age)+" Toddler")
    elif age >= 4 and age < 13:
        print(str(age)+" kid")
    elif age >= 13 and age < 20:
        print(str(age)+" teenager")
    elif age >= 20 and age < 65:
        print(str(age)+" adult")
    else:
        print(str(age)+" elder")

# 5-7 Favorite Fruit

favorite_fruids = ["banana","kiwi","strawberry","cherry"]

if "banana" in favorite_fruids:
    print("Yes, banana!")
if "ananas" not in favorite_fruids:
    print("No ananas?")
if "cherry" in favorite_fruids and "kiwi" in favorite_fruids:
    print("combo")
