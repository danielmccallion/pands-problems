# Daniel Mc Callion
# Program that prints out a random fruit

import random

fruits = ["Apple", "Banana", "Orange", "Grape", "Pear", "Mango"]

# Get a random number between 0 and lenght of fruits list -1
index = random.randint(0, len(fruits)-1)

# Print output
random_fruit = fruits[index]
print(f"A random fruit: {random_fruit}")
