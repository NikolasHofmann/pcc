class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def printbattery(self):
        print("The battery size is " + str(self.battery_size))
        self.battery_size = 50
        print("The new battery size is " + str(self.battery_size))

mybattery = Battery()

mybattery.printbattery()

print("\n\n\n")

# 9-6

print("???")

class Restaurant():


    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name + ".")
        print("The type of cuisine is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant is open.")

    def update_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["strawberry", "chocolate", "vanilla"]

    def show_icecream_flavors(self):
        for flavor in self.flavors:
            print(flavor)


my_ice_stand = IceCreamStand("happy ice time".title(), "Ice Cream")
my_ice_stand.show_icecream_flavors()
print("\n\n\n")

# 9-7

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




class Admin(User):
    def __init__(self, first_name, last_name, email, age, phone_number):
        super().__init__(first_name, last_name, email, age, phone_number)
        #self.privileges = ["can add post", "can delete post", "can ban user"]
        self.mypower = Privileges()

class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "testo"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


    #def show_privileges(self):
     #   for privilege in self.privileges:
      #      print(privilege)


jeff = Admin("Jeff", "Jefferson", "jeff@jeff.jeff", "29", "013495493")

# jeff.show_privileges()


jeff.mypower.show_privileges()

