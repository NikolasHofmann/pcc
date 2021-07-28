class User():
    def __init__(self, first_name, last_name, email, age, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.phone_number = phone_number

    def describe_user(self):
        print(self.first_name.title())
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.phone_number)
    
    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title())
        print("your additional information is: " + "\n" + self.email + "\n" + str(self.age) + "\n" + str(self.phone_number))

