# Daniel Mc Callion
# Program that prints out a dictionary object called current_book
# Prints the author of current_book
# Adds a new attribute with value called ISBN
# Prints out all the values in the current_book using a for loop

current_book = {
    "title": "Harry Skyward",
    "author": "Brandon Potterson",
    "price": 9, 
}

# Print the dictionary object
print(current_book)

# Print only the author
print(current_book["author"])

# Create attribute ISBN with a value
current_book["ISBN"] = "123456"

# Using a for loop iterate through current_book's values
print("The current book has these values:")
for value in current_book.values():
    print(f" => {value}")
