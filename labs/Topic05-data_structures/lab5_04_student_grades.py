# Daniel Mc Callion
# Print out a students subjects and grades using a dict

student = {
    "name": "Mary",
    "subjects": [
        {
            "subject_name": "Programming",
            "grade": 45
        },
        {
            "subject_name": "History",
            "grade": 99
        }
    ]
}

print(f"Student: {student['name']}")

for subject in student["subjects"]:
    print(f"\t {subject['subject_name']} \t: {subject['grade']}")
