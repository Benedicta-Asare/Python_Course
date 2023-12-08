class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nFull name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("Amber", "Smith", 21, "amber@example.com", "San Francisco")
user.describe_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"\nLogin attempt(s): {user.login_attempts}")

user.reset_login_attempts()
print(f"\nLogin attempt(s): {user.login_attempts}")