class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nRestaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")


restaurant_1 = Restaurant('Food Haven', 'Italian')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('Taco Town', 'Mexican')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('Spice Route', 'Indian')
restaurant_3.describe_restaurant()