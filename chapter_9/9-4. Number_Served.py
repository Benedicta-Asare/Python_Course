class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, add_number):
        self.number_served += add_number


restaurant = Restaurant('Sweet Roses', 'Chinese')

restaurant.describe_restaurant()
print(f"\nThe number of customers served is {restaurant.number_served}.")

restaurant.number_served = 10
print(f"The number of customers served is {restaurant.number_served}.")

restaurant.set_number_served(20)
print(f"The number of customers served is {restaurant.number_served}.")

restaurant.increment_number_served(55)
print(f"The number of customers served is {restaurant.number_served}.")
