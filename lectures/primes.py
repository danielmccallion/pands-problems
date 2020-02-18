# Daniel Mc Callion
# Computing the primes

# My list of primes
p = []

# Loop through all of the numbers we're 
# checking for primality
for i in range (2,1000):
    # Assume that i is a prime
    is_prime = True
    # Look through all values j from 2 up
    # to but not including i
    for j in range(2,i):
        # See if j divides i
        if i % j == 0:
            # If it does, i isn't prime exit loop
            # and indicate its not prime
            is_prime = False
            break
    # If i is prime, then append to p
    if is_prime:
        p.append(i)

# Print out the primes
print(p)
