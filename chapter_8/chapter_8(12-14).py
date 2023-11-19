#8-12. Sandwiches

def make_sandwich(*items):
    print("\nThis is the sandwich you ordered with:")
    for item in items:
        print(f" - {item}")

make_sandwich('chicken')
make_sandwich('beef', 'green peppers')
make_sandwich('beef', 'tuna', 'green peppers')


#8-13. User Profile

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('benedicta', 'asare', age=23, location='kumasi', field='mathematics')
print("\n --- User Profile ---")
print(user_profile)


#8-14. Cars

def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', price=47395)
print("\n --- Car Info ---")
print(car)