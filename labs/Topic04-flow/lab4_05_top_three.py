# Daniel Mc Callion
# This program generates 10 random numbers
# It prints them all out, then prints the top three

import random

qty_numbers = 10
qty_top_numbers = 3
start_range = 0
end_range = 100

numbers = []

# Get the random numbers
for i in range (0, qty_numbers):
    numbers.append(random.randint(start_range, end_range))

# Print the random numbers
print(f"{qty_numbers} random numbers\t {numbers}")

# Print the top numbers
numbers.sort(reverse=True)
print(f"The top {qty_top_numbers} are\t\t {numbers[:qty_top_numbers]}")
