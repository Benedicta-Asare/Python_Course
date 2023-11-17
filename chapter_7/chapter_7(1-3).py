#7-1. Rental Car

#message = input("What kind of rental car would you like? ")

#print(f"\nLet me see if I can find you a {message}.")


#7-2. Restaurant Seating

#number = input("\nHow many people are in your dinner group? ")

#number = int(number)

#if number > 8:
#    print("\nYou'll have to wait for a table.")
#else:
#    print("Your table is ready.")


#7-3. Multiples of Ten

question = "\nIf you give me a number, I'll tell you if it's a multiple of 10 or not."
question += "\nEnter a number: "
multiple = input(question)

multiple = int(multiple)

if multiple % 10 == 0:
    print(f"\n{multiple} is a multiple of 10.")
else:
    print(f"\n{multiple} is not a multiple of 10.")