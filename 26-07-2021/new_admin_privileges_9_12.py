from new_user_9_12 import User

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

