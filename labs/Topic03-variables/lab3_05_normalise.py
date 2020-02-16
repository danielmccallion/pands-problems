# Daniel Mc Callion
# Program that reads in a string and strips any leading or trailing spaces.
# It converts all the letters to lowercase and outputs the normalised string.
# The program also outputs the length of the original string and the formatted one.

raw_string = input("Please enter a string: ")
formatted_string = raw_string.strip().lower()

raw_string_length = len(raw_string)
formatted_string_length = len(formatted_string)

# Print output
print(f"That string normalised is: {formatted_string}")
print(f"We reduced the input string from {raw_string_length} to {formatted_string_length} characters")
