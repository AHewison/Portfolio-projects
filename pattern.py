# We need two variables; 
# One with '*' stored as a string
# The second as a counter to multiply how many times we print the string
# Then we use a for loop with a range to limit the amount of times it loops
# We can use conditionals to control whether each loop adds or subtracts an asterix

# Two variables to store the Asterix string and the counter
count = 0
star = "*"


# Then we use a For loop with a range to stop the program when we reach the desired amount
for i in range(1, 10):
    
    # For the first 5 loops we want the amount of asterix's per line to increase
    if i <= 5:
     count += 1
     print(star * count)
    
    # Once we have 5 in a single line, we want each loop to decrease the amount printed
    else:
       count -= 1
       print(star * count)