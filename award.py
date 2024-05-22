"""
Create an integer input for each event in a triathlon, specifying minutes
Calculate the total time taken by adding up the event times
Create an if-elif-else structure to determine the Award the user qualifies for
"""

swim_time = int(input("In minutes, how long did it take you to complete the swimming section of the Triathlon? : "))

cycle_time = int(input("In minutes, how long did it take you to complete the cycling section of the Triathlon? : "))

run_time = int(input("In minutes, how long did it take you to complete the running section of the Triathlon? : "))

total_time = swim_time + cycle_time + run_time
print(f"Your total time is {total_time} minutes.")

if total_time <= 100:
    print("You qualified for the Provincial Colours award!")
elif total_time <= 105:
    print("You qualified for the Provincial Half Colours award!")
elif total_time <= 110:
    print("You qualified for the Provincial Scroll award!")
else:
    print("Sorry, you didn't qualify for an award.")