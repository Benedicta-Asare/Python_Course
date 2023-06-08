#2-3. Personal Message
name = "Benedicta"
print(f"Hello {name}, would you like to learn some Python today?\n")

#2-4. Name Cases
first_name = "Tessy"
print(first_name.lower())
print(first_name.upper())
print(first_name.title())

#2-5. Famous Quote
print('\nAlbert Einstein once said, "A person who never made a mistake never tried anything new."')

#2-6. Famous Quote 2
famous_person = "Maya Angelou"
message = "Do the best you can until you know better. Then when you know better, do better."
print(f'\n{famous_person} once said, "{message}"')

#2-7. stripping Names
name = " Ernestina "
print(f"\n'{name}'")
print(f"\t'{name.lstrip()}'")
print(f"\t'{name.rstrip()}'")
print(f"\t'{name.strip()}'\n")

#2-8. File Extensions
filename = 'python_notes.txt'
filename = filename.removesuffix('.txt')
print(filename)