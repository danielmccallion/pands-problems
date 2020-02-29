# Daniel Mc Callion
# Computing the primes

import math

# My list of primes
p = []

# Loop through all of the numbers we're 
# checking for primality
def is_prime_func(i):
    # Assume that i is a prime
    is_prime = True
    # Look through all values j from 2 up
    # to but not including i
    # for j in range(2,i):
    for j in range(2, math.floor(math.sqrt(i))):
        # See if j divides i
        if i % j == 0:
            # If it does, i isn't prime exit loop
            # and indicate its not prime
            is_prime = False
            break
    return is_prime


# Loop through all of the numbers we're checking for primality#
for i in range(2, 100000):
    if is_prime_func(i):
        p.append(i)

#  Print out the primes
print(p)
