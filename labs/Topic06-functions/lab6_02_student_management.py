# Daniel Mc Callion
# A program that allows a user to add and view students,
# their modules and their grades.

# Function to display a menu and return the choice
def display_menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()

    return choice

# Test the function
users_choice = display_menu()
print(f"You chose {users_choice}")
