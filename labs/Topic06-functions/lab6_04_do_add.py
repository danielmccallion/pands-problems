# Daniel Mc Callion
# The do add function for student management

students = []

def read_modules():
    return []

def do_add():
    current_student = {}
    current_student["name"] = input("Enter name: ")
    current_student["modules"] = read_modules()

    students.append(current_student)

# Test
do_add()
do_add()
print(students)
