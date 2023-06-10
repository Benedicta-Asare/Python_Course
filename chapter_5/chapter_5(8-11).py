#5-8. Hello Admin
usernames = ['tessa', 'bene', 'admin', 'genesis', 'blackprince']

for name in usernames:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name.title()}, thank you for logging in again.")


#5-9. No Users
users = []

if users:
    for name in users:
        print(f"\n\nHello {name.title()}, thank you for logging in again.")
else:
    print("\n\nWe need to find some users!\n\n")


#5-10. Checking Usernames
current_users = ['Tessa', 'BENE', 'Nessa', 'Genesis', 'blackprince']

new_users = ['Bene', 'Tina', 'TESSA', 'gina', 'Niella']

current_users_lower = [x.lower() for x in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"The username '{user}' is already taken. Enter a new username.")
    else:
        print(f"The username '{user}' is available.")


#5-11. Ordinal Numbers
nums = list(range(1,10))

print("\n\nOrdinal numbers:")
for num in nums:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")