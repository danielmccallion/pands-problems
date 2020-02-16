# Daniel Mc Callion
# Check if a number is prime.
# The primes are 2, 3, 5, 7, 11, 13, ...

p = 221
m = 2
is_prime = True

while m < p:
    if p % m == 0:
        is_prime = False
        break
    m = m + 1

if is_prime:
    print(f"{p} is a prime number.")
else:
    print(f"{p} is not prime.")

# Use for instead of while
p = 347
is_prime = True

for m in range(2, p-1):
    if p % m == 0:
        is_prime = False
        break

if is_prime:
    print(f"{p} is a prime number.")
else:
    print(f"{p} is not prime.")

print("Thank you for running my program.")
