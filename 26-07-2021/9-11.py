from module_9_11 import User, Admin

jeff = Admin("Jeff", "Jefferson", "jeff@jeff.jeff", "29", "013495493")

print("User:")
jeff.describe_user()
print("\nPrivileges:")
jeff.mypower.show_privileges()