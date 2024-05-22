# Ask user for input number
# Repeat Question until user enters desired number
# Create 2 variables: one that adds the number the user inputs, the other is a count that increases by 1 each loop
# Create a while loop that increases count by 1 for each loop, and adds the input value to a total
# Create a variable for when the while loop condition is broken, that calculates the average input

user_number = int(input("Please enter any number (But you shouldn't enter -1) : "))

user_total = 0
user_count = 0

while user_number != -1:
    user_count += 1
    user_total += user_number
    user_number = int(input("Please enter another number (You really shouldn't enter -1 now) : "))

user_average = user_total / user_count

print(f"You have entered the dreaded -1 and broken the Average Genie free from his Loopy chains! Your average input was {user_average}")