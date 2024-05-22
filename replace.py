"""
Create a variable with the value "The!quick!brown!fox!jumps!over!the!lazy!dog."
Reprint using the replace() function to replace every ! with a space
Reprint the sentence in upper case
Reverse the string

"""

string = "The!quick!brown!fox!jumps!over!the!lazy!dog."

changed_string = string.replace('!' , ' ')
print(changed_string)

upper_changed_string = changed_string.upper()
print(upper_changed_string)

# using '[::-1]', we don't need to find the length of the string as this will cover then entire string. If we wanted to reverse a specific part we could enter in a start and end position of characters to reverse
print(upper_changed_string[::-1])

