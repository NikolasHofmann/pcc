colors = ["red","green","blue","orange"]

for color in colors[:3]:
    print(color.title())

# [:] takes the entire list
print(colors[:])

mystuff = ["backpack","laptop","guitar"]

lilis_stuff = mystuff

print (lilis_stuff)

mystuff.append("pullover")

# lilis stuff is the same as mystuff

print(mystuff)
print(lilis_stuff)


mystuff = ["backpack","laptop","guitar"]

lilis_stuff = mystuff[:]

mystuff.append("pullover")

# lilis stuff is what mystuff was at he point of assigning

print(mystuff)
print(lilis_stuff)






