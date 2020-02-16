# Daniel Mc Callion
# Reads in two numbers and outputs the result of the first number divided by the second
# Result should be an integer with the remainder also provided

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x / y)
remainder = x % y
print(f"{x} divided by {y} is {answer} with remainder {remainder}")
