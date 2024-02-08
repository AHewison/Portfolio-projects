# Create a calculator that varies depending on user input
# First we need to receive user input for which calculator they want to use
# Then we need to convert it into lower case 
# This is so that the condition of the if statement is met

import math

user_choice = input("""
      investment - to calculate the amount of interest you'll earn on your investment
      bond       - to calculate the amount you'll have to pay on a home loan

      Enter either 'investment' or 'bond' from the menu above to proceed:     
      
      """)

user_choice_lower = user_choice.lower()


# For 'investment' we need 4 inputs: deposit amount, interest rate, length of time and interest type
# We then need two different calculations and outputs based on interest type

if user_choice_lower == "investment":
    user_deposit = int(input("How much will you deposit? : "))
    user_interest = float(input("What is the interest rate? (Please do not enter the '%' symbol) : "))
    user_years = int(input("How many years will this be invested for? : "))
    interest = input("Will the interest be 'simple' or 'compound'? Please enter either 'Simple' or 'Compound': ")
    interest_captialized = interest.capitalize()
    if interest_captialized == "Simple":
        amount = user_deposit * (1 + (user_interest / 100) * user_years)
        print(f"As you have selected Simple interest, after {user_years} years the amount will be : {int(amount)}")
    elif interest_captialized == "Compound":
        amount = user_deposit * math.pow((1 + user_interest / 100), user_years)
        print(f"As you have selected Compound interest, after {user_years} years the amount will be : {int(amount)}")
    else:
        interest = input("Please enter only Simple if you would like the simple interest calculator, or Compound for the compound interest calculator.")


# For 'bond' we need 3 inputs: house value, interest rate and the amount of months to repay the loan

elif user_choice_lower == "bond":
    user_housevalue = int(input("What is the value of your property? : "))
    user_interest = float(input("What is the interest rate? (Please do not enter the '%' symbol) : "))
    monthly_interest = (user_interest / 100) / 12
    user_months = int(input("How many months do you plan on taking to repay the bond? : "))
    monthly_payment = (monthly_interest * user_housevalue) / (1 - (1 + monthly_interest)**(-user_months))
    print(f"The monthly amount you will have to repay is {int(monthly_payment)}")
    
# Then we need an error message if anything other than investment or bond is entered at the beginning
        
else:
    print("This input is not recognised, please enter either 'investment' or 'bond'.")