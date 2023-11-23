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
        print(f"\nHello {self.first_name}, welcome!")


class Admin(User):
    def __init__(self, first_name, last_name, age, email, location):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("\nAdmin's privileges:")
        for privilege in self.privileges:
            print("-", privilege)


admin = Admin('Tracy', 'Scott', '25', 'tracy@example.com', 'London')
admin.describe_user()
admin.greet_user()
admin.show_privileges()