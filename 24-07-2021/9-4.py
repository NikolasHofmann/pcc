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


my_restaurant = Restaurant("Niko's", "Burgers")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print("\nI can also call the name like this: " + my_restaurant.restaurant_name)
print("I can also call the type of cuisine like this: " + my_restaurant.cuisine_type + "\n")

other_restaurant = Restaurant("Otherplace", "Otherfoods")
maurice_retaurant = Restaurant("Maurice's", "La bella comida")

other_restaurant.describe_restaurant()
maurice_retaurant.describe_restaurant()
print("\n\n\n")

restaurant = Restaurant("Alfonso's", " Pizza")
print("Welcome to " + restaurant.restaurant_name + restaurant.cuisine_type)
print("\nWe have served " + str(restaurant.number_served) + " " + restaurant.cuisine_type.lower() + "s.")

restaurant.update_number_served(100)
print("...updated the number served to " + str(restaurant.number_served))

restaurant.increment_number_served(20)
print("We have served more pizzas. Now it is " + str(restaurant.number_served) + ".")