from pathlib import Path

# Collecting names from users
names = []
while True:
    name = input("Please enter your name (enter q to quit): ")
    if name.lower() == 'q':
        break
    names.append(name + '\n')

# Writing names to a file
path = Path('guest_book.txt')

with path.open(mode='a') as file:   # 'a' mode for appending
    file.writelines(names)