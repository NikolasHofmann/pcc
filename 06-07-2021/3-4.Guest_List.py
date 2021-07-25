#send invitation
Guest_List = ["Frederic Chopin", "Lilly Turek", "Dennis"]

for guest in Guest_List:
    print("Dear", guest,"please join me for Dinner this evening.")

#3-5 changing guest list

print(Guest_List[0] + "can not make it to the dinner party...")
newguest = "Mirco"
print("That's why we are inviting " + newguest)

Guest_List[0] = newguest

for guest in Guest_List:
    print("Dear", guest,"please join me for Dinner this evening.")

Guest_List.insert(0, "Anthony Kiedis")

print(Guest_List)

Guest_List.insert(2,"Nicole Hamm")

print(Guest_List)

Guest_List.append("Charles Ives")

print(Guest_List)

for guest in Guest_List:
    print("Dear", guest,"please join me for Dinner this evening.")

#3-7 Shrinking Guest List

print("Unfortunately the new table won't arrive in time. Thats why I can only invite two guests...")

print("We have invited " + str(len(Guest_List)) + " persons")

while len(Guest_List) > 2:
    popped_guest = Guest_List.pop(-1)
    print("I am sorry, " + popped_guest + " but you can not come to my dinner party...")

for guest in Guest_List:
    print("Dear " + guest + " you remain invited, see you this evening!")

for i in range(len(Guest_List)):
    popped_guest = Guest_List.pop()
    print(popped_guest + " was removed...")

print(Guest_List)

Guest_List == []

    