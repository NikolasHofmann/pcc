locations = ["Medellin","Buenos Aires","Mexico City","Thailand","Caribbean"]

print(locations)
print(sorted(locations))
print("The original list is still here...\n")
print(locations)

print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)

#a method like .sort() changes the actual object. A function like sorted() can
#have a output but it doesnt change the predefined object

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)