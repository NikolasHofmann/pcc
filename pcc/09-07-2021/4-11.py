pizzas = ["cheese","pepperoni","spinach"]

for pizza in pizzas:
    print("I really like "+pizza+"-pizza yum\n")

print("I really like pizza!")

friend_pizzas = pizzas[:]

pizzas.append("veggie")
friend_pizzas.append("onion")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)