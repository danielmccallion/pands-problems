# Daniel Mc Callion
# The do add and read modules functions for student management

students = []

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

def do_add():
    current_student = {}
    current_student["name"] = input("Enter name: ")
    current_student["modules"] = read_modules()

    students.append(current_student)

# Test
do_add()
do_add()
print(students)
