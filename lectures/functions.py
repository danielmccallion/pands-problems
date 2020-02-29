# Daniel Mc Callion
# A function to square numbers.

import math

def power(x, y):
    ans = x
    y = y - 1
    while y > 0:
        ans = ans * x
        y = y - 1
    return ans

def f(x):
    ans = (100 * power(x, 2) + 10 * power(x, 3)) // 100
    ans = ans - (power(x, 3) // 10)
    return ans


# Loop through all of the numbers we're 
# checking for primality
def is_prime_func(i):
    # Look through all values j from 2 up
    # to but not including i
    for j in range(2, math.floor(math.sqrt(i))):
        # See if j divides i
        if i % j == 0:
            # If it does, i isn't prime exit loop
            # and indicate its not prime
            return False
    return True
