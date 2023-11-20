# 9-1. Restaurant 

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


restaurant = Restaurant('Sweet Roses', 'Chinese')

print(f"Restaurant name: {restaurant.restaurant_name}")
print(f"Cuisine type: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()