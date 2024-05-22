"""
Create a series of conditionals that change output based on number inputted
Order of conditional arguments should be Highest age -> Lowest age
If order was reversed, and user input is 70, you would receive output for 40+ and 65+
"""

age = int(input("What is your age? : "))

if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")