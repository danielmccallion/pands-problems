# Daniel Mc Callion
# Computing the primes

from functions import is_prime_func

# My list of primes
p = []

# Loop through all of the numbers we're checking for primality#
for i in range(2, 100000):
    if is_prime_func(i):
        p.append(i)

#  Print out the primes
print(p)
