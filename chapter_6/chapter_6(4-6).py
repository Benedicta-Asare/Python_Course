#6-4. Glossary 2
glossary = {
    'variable': 'A label that is assigned to a value.',
    'float': 'A number with a decimal point.',
    'string': 'A series of characters.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'data type': 'Specifies the type of data a variable can hold, such as integers, floating-point numbers, strings, etc.', 
    'loop': 'A control flow statement that allows code to be executed repeatedly, such as while and for loops.', 
    'index': 'A numeric value used to access elements in a sequence (eg. lists, strings) based on their position.', 
    'boolean': 'A data type that represents either True or False.', 
    'conditional statement': 'A statement that performs diifferent actions based on certain conditions, using if, else and elif.'
}

for word, meaning in glossary.items():
    print(f"\n{word.title()}: {meaning}")


#6-5. Rivers
rivers = {
    'nile': 'egypt', 
    'yangtze': 'china',
    'mississippi': 'united states'
} 

print("\n\nRivers:")
for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.\n")


#6-6. Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people = ['gene', 'sarah', 'prince', 'phil', 'edward']

for name in people:
    if name in favorite_languages:
        print(f"\n{name.title()}, thank you for responding.")
    else:
        print(f"\n{name.title()}, you're invited to take the poll.")
