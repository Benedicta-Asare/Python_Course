guests = ["Gina", "Daniella", "Tessa"]

print(f"Hello {guests[0]}, you are invited to my dinner.")
print(f"Hello {guests[1]}, you are invited to my dinner.")
print(f"Hello {guests[2]}, you are invited to my dinner.\n")

print(f"{guests[1]} can't make it to the dinner.")
guests[1] = "Stacy"

print(f"\nHello {guests[0]}, you are invited to my dinner.")
print(f"Hello {guests[1]}, you are invited to my dinner.")
print(f"Hello {guests[2]}, you are invited to my dinner.")

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

print(f"I'm inviting {len(guests)} people to the dinner.")