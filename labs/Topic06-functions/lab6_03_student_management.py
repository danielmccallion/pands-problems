# Daniel Mc Callion
# A program that allows a user to add and view students,
# their modules and their grades.

# Function to display a menu and return the choice
def display_menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip().lower()

    return choice

# Future for adding a student
def do_add():
    print("in adding")

# Future for viewing a student
def do_view():
    print("in viewing")

# Main Program
users_choice = display_menu()
while users_choice != "q":
    if users_choice == "a":
        do_add()
    elif users_choice == "v":
        do_view()
    elif users_choice != "q":
        print("\n\nPlease select either a, v or q\n\n")
    users_choice = display_menu()
