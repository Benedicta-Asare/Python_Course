import random

# Creating a list containing numbers and letters
arr = [1, 3, 5, 7, 10, 15, 20, 24, 30, 36, 'a', 'b', 'c', 'd', 'e']

# Randomly selecting 4 elements from the list
winning_ticket = random.sample(arr, 4)

print(f"Selected elements: {winning_ticket}")
print("Any ticket matching these elements wins a prize.")