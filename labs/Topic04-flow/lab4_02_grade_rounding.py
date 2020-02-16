# Daniel Mc Callion
# This program reads in a students percentage mark and 
# prints out the corresponding grade using rounding.

percentage = float(input("Enter the percentage: "))

# Round input
percentage_rounded = round(percentage)

if percentage_rounded < 0 or percentage_rounded > 100: 
    # Should throw an error
    print("Please enter a number between 0 and 100")
elif percentage_rounded < 40: # Betweeen 0 and 40
    print("Fail")
elif percentage_rounded < 50: # Between 40 and 49
    print("Pass")
elif percentage_rounded < 60: # Between 50 and 59
    print("Merit")
elif percentage_rounded < 70: # Between 60 and 69
    print("Merit2")
else: # Between 70 and 100
    print("Distinction")
