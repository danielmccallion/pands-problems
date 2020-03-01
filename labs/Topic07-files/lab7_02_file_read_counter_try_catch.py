# Daniel Mc Callion
# Reads the number of times a file has been run and writes it back.
# Uses try and catch to stop error if file doesnt exist


# Function to read a file and return the number it contains
def read_number(file_to_read):
    try:
        with open(file_to_read) as f:
            count = int(f.read())
            return count
    except IOError:
        # This file will be created when we write back.
        # No file assumes first time running.
        # 0 previous runs
        return 0


# Function to write the number of times a file has been ran 
def write_number(file_to_read, count):
    with open(file_to_read, "wt") as f:
        # Write takes a string so have to convert int
        f.write(str(count))


filename = "count.txt"
number = read_number(filename)
number += 1
print(f"We have run this program {number} times.")
write_number(filename, number)
