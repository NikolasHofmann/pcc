# create a second list with stuff that we want to exclude and remove those
# items from the list

songs =["nocturne_op_9","lala_land","under_the_bridge"]

print([songs])

exclude = []

exclude.extend(["under_the_bridge","lala_land"])
print (exclude)

for item in exclude:
    if item in songs:
        songs.remove(item)
        print("\n"+item+" was removed from songs...")

print(songs)

#check if list is empty

requested_toppings = []

if requested_toppings:
    print("List is not empty")
else:
    print("List is empty")

#5-8

usernames = ["admin","anthony","pizza_dude","mum","bro_dude"]

#first check that usernames is not empty...

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello, special one...")
        else:
            print("Hello, "+username)
else:
    print("We need to find users")


#5-10

current_users = ["admin","anthony","pizza_dude","mum","bro_dude"]

new_users = ["lilly","theresa","pizza_DUDE","simon","daniel","Anthony"]

current_users_case = [user.lower() for user in current_users]

new_users_case = [user.lower() for user in new_users]

print("The current users case list is "+str(current_users_case))
print("The new users case list is "+str(new_users_case)+"\n\n\n")

for new_user in new_users:
    if new_user.lower() in current_users_case:
        print(new_user+" has already been used, please enter another username...")
    else:
        print(new_user+" is avaiable.")

numbers = []
for number in range(1,10):
    numbers.append(number)

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")



