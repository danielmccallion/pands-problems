# Daniel Mc Callion
# A program that takes in a number from the user and subtracts 10% from it
# If the number is less than 0 an error is thrown

percent = 0.9 

# get number from user
user_number = float(input("Enter number: "))

# check if number is above 0
if user_number < 0:
    raise ValueError(f"Number entered should be 0 or above")

# minus 10%
new_number = user_number * percent

# Output result
print(f"{user_number} minus 10% is {new_number}")
