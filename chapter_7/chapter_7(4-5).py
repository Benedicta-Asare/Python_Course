#7-4. Pizza Toppings

print("\nI'm going to ask you to give a series of toppings for your pizza.")
message = "\nEnter a pizza topping:"
message += "\n(Enter 'q' when you're done.) "

result = " "

while result != 'q':
    result = input(message)
    if result != 'q':
        print(f"I'll add {result} to your pizza.")


#7-5. Movie Tickets

while True:
    age = input("\nEnter your age: ")
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif age >= 3 and age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

    user_input = input("\nWould you like to get another ticket? (Type 'yes' to continue or 'no' to exit.) ")
    if user_input == 'no':
        break
    else:
        continue
