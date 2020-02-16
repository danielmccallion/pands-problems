# Daniel Mc Callion
# The program reads in numbers until user enters a 0
# Prints them all back out along with their average

numbers = []

# Get the first number
number = int(input("Enter number (0 to quit): "))

# Keep testing if number is zero
while number != 0:
    numbers.append(number)

    # Read the next number
    number = int(input("Enter another (0 to quit): "))

for value in numbers:
    print(value)

# Average should be a float, protect from div 0
if numbers:
    average = float(sum(numbers)) / len(numbers)
    print(f"The average is {average:.1f}")
else:
    print("No numbers were entered")