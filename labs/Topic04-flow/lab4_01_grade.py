# Daniel Mc Callion
# This program reads in a students percentage mark and 
# prints out the corresponding grade.

percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100: 
    # Should throw an error
    print("Please enter a number between 0 and 100")
elif percentage < 40: # Betweeen 0 and 40
    print("Fail")
elif percentage < 50: # Between 40 and 49
    print("Pass")
elif percentage < 60: # Between 50 and 59
    print("Merit")
elif percentage < 70: # Between 60 and 69
    print("Merit2")
else: # Between 70 and 100
    print("Distinction")
