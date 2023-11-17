#7-8. Deli

sandwich_orders = ['beef', 'chicken', 'vegetable', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nThis is a list of sandwiches made:")
for name in finished_sandwiches:
    print(name)


#7-9. No Pastrami

sandwich_orders = ['beef', 'pastrami', 'chicken', 'pastrami', 'vegetable', 'pastrami', 'tuna']

print("\nThe deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = sandwich_orders
print(finished_sandwiches)


#7-10. Dream Vacation

results = {}
active = True

while active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    results[name] = place

    repeat = input("\nWould anyone like to respond? (yes/no) ")
    if repeat == 'no':
        active = False

print("\n--- Poll Results ---")
for name, place in results.items():
    print(f"{name} would like to visit {place}.")   

