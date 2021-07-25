class User():
    def __init__(self, first_name, last_name, email, age, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.phone_number = phone_number
        self.login_attemps = 0

    def describe_user(self):
        print(self.first_name.title())
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.phone_number)
    
    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title())
        print("your additional information is: " + "\n" + self.email + "\n" + str(self.age) + "\n" + str(self.phone_number))

    def increment_login_attemps(self):
        self.login_attemps = self.login_attemps + 1

    def reset_login_attemps(self):
        self.login_attemps = 0        

Lilli = User("Lillian", "turek", "lala@lala", 18, 123345)
Nikolas = User("Nikolas", "Hofmann", "nikolas@email", 29, 53453453)

print("\n\n")
Lilli.describe_user()
print("\n")
Lilli.greet_user()
print("\n")
print("\n")
Nikolas.describe_user()
print("\n")
Nikolas.greet_user()
print("\n\n")

new_user = User("Testo", "Rino", "testo@rino", 22, 1235242342)
print(new_user.last_name)
print(new_user.phone_number)
print(new_user.login_attemps)
value = input("\nPlease tell me by how much I should increment login attemps.\n")
value = int(value)
if value == 0:
    print("\nnot a valid increment")
else:
    for i in range(0, value):
        new_user.increment_login_attemps()
        print("Incremented by 1")

print("\nThe login attempt number is " + str(new_user.login_attemps))

new_user.reset_login_attemps()
print("The login attempts were resetted...\n")
print(new_user.login_attemps)

