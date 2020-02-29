# Daniel Mc Callion
# A program that allows a user to add and view students,
# their modules and their grades.

# The array to store a students
students = []


# Function to display a menu and return the choice
def display_menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip().lower()

    return choice


# Displays students modules
def display_modules(modules):
    print("\tSubject\t\tGrade")
    for module in modules:
        print(f"\t{module['name']}\t\t{module['grade']}")


# Displays students data
def do_view():
    for current_student in students:
        print(f"Student: {current_student['name']}")
        display_modules(current_student["modules"])


# Reads in a students modules and grades from a user
def read_modules():
    modules = []
    module_name = input("\tEnter the first module name (blank to quit): ").strip()

    while module_name != "":
        module = {}
        module["name"] = module_name
        module["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)

        module_name = input("\tEnter the next module name (blank to quit): ").strip()

    return modules


# Lets a user enter in a students details
def do_add():
    current_student = {}
    current_student["name"] = input("Enter name: ")
    current_student["modules"] = read_modules()

    students.append(current_student)


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
