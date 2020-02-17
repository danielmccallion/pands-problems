# Daniel Mc Callion
# The program reads in students name until a blank is entered
# Prints all the names out after

students = []

# Get the firstname
firstname = input("Enter firstname (blank to quit): ").strip()

# Keep testing if firstname is blank
while firstname != "":
    student = {"firstname": firstname}
    lastname = input("Enter lastname: ").strip()
    student["lastname"] = lastname
    students.append(student)

    # Read the next students firstname
    firstname = input("Enter firstname of next student (blank to quit): ").strip()

if students:
    print("Here are the students you entered:")
    for current_student in students:
        print(f"{current_student['firstname']} {current_student['lastname']}")
else:
    print("You did not enter any students")
