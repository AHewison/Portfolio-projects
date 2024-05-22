# The first part of the task is to alternate the case of each character.
# To do this we will use two variables, one containing the string and another that is empty for the For loop to return altered characters to
# We can assign each character a index value, then use the condition of whether this value is even or odd to affect the case of each character
# We can then put each character back into an empty variable to create our string

# First, we create our variables
string = "I am learning to code"
output = ""

# Here, we use i as the index number and 'character' as the variable assigned to that index number
for i, character in enumerate(string):
        if i % 2 == 0:
             output += string[i].upper()
        else:
             output += string[i].lower()

print(output)

# The second part of the task is to alternate the case of each word in the given string
# To do this, first we can split the string using spaces as the key for where the string will be split.
# This will return a list, with each word being a seperate item in the list. 
# We can use a similar strategy as before, we can create an empty list to return the iterated values.
# We can use the .append() function to add ach word to the ed of the list after we have iterated over it.
# Once the for loop is finished, we can use the .join() function to add each element of the list together with a space in between

# Here we create a list by splitting the given string by using the spaces as our reference points. We also create an empty list.
string_words = string.split(" ")
words_output = []

# Now we can iterate over each word to assign it a value, and change it's case depending on whether the index value is odd or even.
for i, word in enumerate(string_words):
        if i % 2 == 0:
            words_output.append(word.lower())
        else:
            words_output.append(word.upper())

# We can use the .join() function now to add the items in the list together with spaces in between
print(" ".join(words_output))

