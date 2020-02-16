# Daniel Mc Callion
# Program that prints out a random number using a range inputted by a user

import random

# Get range from user
print("Enter a range to get a random number from...")
range_start = int(input("Start of range: "))
range_end = int(input("End of range: "))

# Print output
number = random.randint(range_start,range_end)
print(f"Here is a random number between {range_start} and {range_end}: {number}")
