class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"\nFull name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"\nHello {self.first_name}!")

print("\n --- User Profile ---")

user1 = User("Mary", "Doe", 21, "mary@example.com", "New York")
user1.describe_user()
user1.greet_user()

user2 = User("Amber", "Smith", 25, "amber@example.com", "San Francisco")
user2.describe_user()
user2.greet_user()

user3 = User("James", "Johnson", 23, "james@example.com", "London")
user3.describe_user()
user3.greet_user()
