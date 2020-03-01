# Daniel Mc Callion
# Reads the number of times a file has been run and writes it back.
# If the file doesnt exist it creates it. It checks using os first
# if it exists or not.

import os.path


# Function to read a file and return the number it contains
def read_number(file_to_read):
    with open(file_to_read) as f:
        count = int(f.read())
        return count


# Function to write the number of times a file has been ran 
def write_number(file_to_read, count):
    with open(file_to_read, "wt") as f:
        # Write takes a string so have to convert int
        f.write(str(count))


filename = "count.txt"

# Uses os.path to check if the file exist first, if not it creates it
if not os.path.isfile(filename):
    print("File does not exist")
    # Initialise file
    write_number(filename, 0)

number = read_number(filename)
number += 1
print(f"We have run this program {number} times.")
write_number(filename, number)
