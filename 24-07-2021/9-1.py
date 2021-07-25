class Restaurant():


    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name + ".")
        print("The type of cuisine is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant is open.")

my_restaurant = Restaurant("Niko's", "Burgers")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print("\nI can also call the name like this: " + my_restaurant.restaurant_name)
print("I can also call the type of cuisine like this: " + my_restaurant.cuisine_type + "\n")

other_restaurant = Restaurant("Otherplace", "Otherfoods")
maurice_retaurant = Restaurant("Maurice's", "La bella comida")

other_restaurant.describe_restaurant()
maurice_retaurant.describe_restaurant()

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
