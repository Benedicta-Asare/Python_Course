print("\nGive me two nummbers, and I'll find the sum")
print("Enter q to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number.lower() == 'q':
        break

    second_number = input("Second number: ")
    if second_number.lower() == 'q':
        break

    try:
        sum = int(first_number) + int(second_number)
    except ValueError:
        print("Sorry, your input is invalid.")
    else:
        print(f"Ans = {sum}")