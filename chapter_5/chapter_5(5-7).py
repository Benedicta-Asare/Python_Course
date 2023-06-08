#5-5. Alien Colors #3
alien_color = "yellow"

if alien_color == "green":
    print("\nYou earned 5 points.")
elif alien_color == "yellow":
    print("\nYou earned 10 points.")
else:
    print("\nYou earned 15 points.")


#5-6. Stages of Life
age = 25

if age < 2:
    print("\nYou are a baby.")
elif age >= 2 and age < 4:
    print("\nYou are a toddler.")
elif age >= 4 and age < 13:
    print("\nYou are a kid.")
elif age >= 13 and age < 20:
    print("\nYou are a teenager.")
elif age >= 20 and age < 65:
    print("\nYou are an adult.")
else:
    print("\nYou are an elder.")


#5-7. Favorite Fruit
favorite_fruits = ["orange", "apple", "pineapple"]

if "orange" in favorite_fruits:
    print("\nI really like oranges!")
if "banana" in favorite_fruits:
    print("I really like bananas!")
if "apple" in favorite_fruits:
    print("I really like apples!")
if "mango" in favorite_fruits:
    print("I really like mangoes!")
if "pineapple" in favorite_fruits:
    print("I really like pineapples!")