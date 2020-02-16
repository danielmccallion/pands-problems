# Daniel Mc Callion
# Program that creates a dictionary using a constructor and then outputs the dictionary

student = dict(firstname= "Joe", lastname="Bloggs", age=25, height=180,
country="Ireland", alive=True)

# Print the dictionary object
print(student)

# Print only the firstname in student
print(student["firstname"])

# Create attribute hair with a value
student["hair"] = "Brown"

# Using a for loop iterate through student's values
print("The student has these values:")
for value in student.values():
    print(f" => {value}")
