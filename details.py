"""
Create a variable and input for each detail:
name
age
house number
street name

print all details in one sentence using a formatted string

"""

user_name = input("Hello! What is your name? : ")

user_age = input("And what is your age? : ")

user_streetname = input("Thanks! What is the name of the street that you live on? : ")

user_housenumber = input(f"And on {user_streetname}, what number is your home? : ")

print(f"So, your name is {user_name}, you are {user_age} years old, and you live at number {user_housenumber} on {user_streetname}")