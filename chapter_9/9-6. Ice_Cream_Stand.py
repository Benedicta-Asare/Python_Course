class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name, cuisine_type='Ice Cream Shop')
        self.flavors = flavors

    def display_flavors(self):
        print("Ice cream flavors available:")
        for flavor in self.flavors:
            print(flavor)


icecreamstand = IceCreamStand('SweetTreats', ['Vanilla', 'Chocolate', 'Strawberry'])
icecreamstand.describe_restaurant()
icecreamstand.display_flavors()

