#6-7. People

person_1 = {'first_name': 'Tessa', 'last_name': 'Lynn', 'age': 21, 'city': 'London'}
person_2 = {'first_name': 'Scarlet', 'last_name': 'Roberts', 'age': 20, 'city': 'Sydney'}
person_3 = {'first_name': 'Emma', 'last_name': 'Stone', 'age': 20, 'city': 'Miami'}

people = [person_1, person_2, person_3]

print("\nUsers' info")

for person in people:
    print(person)


#6-8. Pets

pet_1 = {'name': 'Milo', 'kind': 'dog', 'owner': 'Cooper'}
pet_2 = {'name': 'Luna', 'kind': 'parrot', 'owner': 'Stacy'}
pet_3 = {'name': 'Penny', 'kind': 'cat', 'owner': 'Kasie'}

pets = [pet_1, pet_2, pet_3]

print("\nPets' list")

for pet in pets:
    print(pet)


#6-9. Favorite Places

favorite_places = {
    'mandy': ['dubai', 'korea'],
    'mark': ['los angelos'],
    'gina': ['korea', 'paris', 'new york']
}

print("\nFavorite places")

for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{name.title()}'s favorite places are:")
        for place in places:
            print(f"\t{place.title()}")
    else:
        print(f"\n{name.title()}'s favorite place is {place.title()}.")


#6-10. Favorite Numbers

favorite_numbers = {
    'sandy': [9, 11, 15],
    'prince': [7, 23],
    'nessa': [1, 3],
    'stacy': [1, 5],
    'ransford': [1, 7, 10],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers: ")
    print(numbers)


#6-11. Cities

cities = {
    'miami': {
        'country': '',
        'population': '',
        'fact': '',
    },

    'paris': {
        'country': '',
        'population': '',
        'fact': '',
    },

    'sydney': {
        'country': '',
        'population': '',
        'fact': '',
    },
}

for city, city_info in cities.item():
    print(f"\nCity: {city.title()}")

    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact.title()}")