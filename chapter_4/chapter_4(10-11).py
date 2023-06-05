#4-10. Slices
animals = ["dog", "cat", "parrot", "snake", "elephant"]

print("The first three items in the list are:")
print(animals[:3])

print("\nThree items from the middle of the list are:")
print(animals[1:4])

print("\nThe last three items in the list are:")
print(animals[-3:])


#4-11. My Pizzas, Your Pizzas
pizzas = ["chicken", "pepperoni", "beef"]

friend_pizzas = pizzas[:]

pizzas.append("cheese")
friend_pizzas.append("tuna")

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)