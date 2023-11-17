#8-3. T-Shirt

def make_shirt(size, message):
    print(f"\nThe size of the T-shirt is {size} and the message printed on it is '{message}'.")

make_shirt('medium', 'I love coding')
make_shirt(size='large', message='Nothing is impossible')


#8-4. Large Shirts

def make_shirt(size='large', message='I love Python'):
    print(f"\nThe size of the T-shirt is {size} and the message printed on it is '{message}'.")

make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='I love music')


#8-5. Cities

def describe_city(city, country='Ghana'):
    print(f"\n{city.title()} is in {country.title()}.")

describe_city('kumasi')
describe_city('tokyo', 'japan')
describe_city('delhi', 'india')
