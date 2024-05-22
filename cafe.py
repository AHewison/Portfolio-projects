# We will make a menu of items, with 2 dictionaries.
# One dictionary for prices, another for stock amounts.
# Then we will loop over these, multiplying the values against each other.
# Thse will then be added to a total value to find the value of all the stock.


# A list of items which will act as our Keys for the dictionaries.
menu = [ "coffee", "tea", "carrot cake", "shortbread", "cheese toastie"]

# A dictionary with our List being the Key an stock amounts being the values.
stock = { "coffee" : 10,
          "tea" : 7, 
          "carrot cake" : 8, 
          "shortbread" : 5, 
          "cheese toastie" : 2
          }

# A dictionary with our List being the Key an price amounts being the values.
price = { "coffee" : 3,
          "tea" : 2, 
          "carrot cake" : 4, 
          "shortbread" : 1, 
          "cheese toastie" : 5 
          }

# A variable with a start value of zero to add the item_value to in each loop
total_stock = 0

# Now we will loop through both dictionaries, using our menu as the range and 'item' as each Key.
# We can then use a nw variable to multiply the Values of each key from the stock and price dictionaries together and add this variable to thetotal_value
for items in menu:
    item_value = (stock[items] * price[items])
    total_stock += item_value

print(f"The total value of the stock is £{total_stock}")
