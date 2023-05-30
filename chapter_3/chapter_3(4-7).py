# Guests List
guests = ["Gina", "Daniella", "Tessa"]

print(f"Hello {guests[0]}, you are invited to my dinner.")
print(f"Hello {guests[1]}, you are invited to my dinner.")
print(f"Hello {guests[2]}, you are invited to my dinner.\n")

# Changing Guest List
print(f"{guests[1]} can't make it to the dinner.")
guests[1] = "Stacy"

print(f"\nHello {guests[0]}, you are invited to my dinner.")
print(f"Hello {guests[1]}, you are invited to my dinner.")
print(f"Hello {guests[2]}, you are invited to my dinner.")

# More Guests
print("\nI have found a bigger table.")

guests.insert(0, "Eunice")
guests.insert(2, "Blankson")
guests.append("Prince")

print(f"\nHello {guests[0]}, you are invited to my dinner.")
print(f"Hello {guests[1]}, you are invited to my dinner.")
print(f"Hello {guests[2]}, you are invited to my dinner.")
print(f"Hello {guests[3]}, you are invited to my dinner.")
print(f"Hello {guests[4]}, you are invited to my dinner.")
print(f"Hello {guests[5]}, you are invited to my dinner.\n")

# Shrinking Guest List
print("I can invite only two people for the dinner.\n")

popped_guest_1 = guests.pop()
print(f"Hello {popped_guest_1}, I'm sorry I can't invite you to the dinner.")

popped_guest_2 = guests.pop()
print(f"Hello {popped_guest_2}, I'm sorry I can't invite you to the dinner.")

popped_guest_3 = guests.pop()
print(f"Hello {popped_guest_3}, I'm sorry I can't invite you to the dinner.")

popped_guest_4 = guests.pop()
print(f"Hello {popped_guest_4}, I'm sorry I can't invite you to the dinner.")

print(f"\nHello {guests[0]}, you are still invited to my dinner.")
print(f"Hello {guests[1]}, you are still invited to my dinner.\n")

del guests[1]
del guests[0]
print(guests)