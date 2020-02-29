# Daniel Mc Callion
# A function to square numbers.

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

print(f(2))