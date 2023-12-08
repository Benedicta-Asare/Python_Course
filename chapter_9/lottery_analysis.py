import random

# Define your ticket
my_ticket = [3, 15, 23, 30]

attempts = 0

# loop until the ticket matches the randomly drawn numbers
while True:
    drawn_numbers = random.sample(range(1, 50), 4)
    
    attempts += 1

    # Check if there is a match
    if drawn_numbers == my_ticket:
        break

# Report the number of attempts taken to win
print(f"It took {attempts} attempts to win the lottery with ticket {my_ticket}.")