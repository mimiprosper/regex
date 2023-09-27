import re

# findall() --> Print a list of all matches:
txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)

# # Return an empty list if no match was found:
# x = re.findall('Portugal', txt)
# print(x)

# # search() --> Search for the first white-space character in the string:
# x = re.search('\s', txt)
# print("The first white-space character is located in position:", x.start())

# # Make a search that returns no match, None:
# x = re.search('Portugal', txt)
# print(x)

# # split() --> Split at each white-space character:
# x = re.split('\s', txt)
# print(x)

# # Split the string only at the first occurrence:
# x = re.split('\s', txt, 1)
# print(x)

# # sub() --> Replace every white-space character with the number 9:
# x = re.sub('\s', '9', txt)
# print(x)

# # Replace the first 2 occurrences:
# x = re.sub('\s', '9', txt, 2 )
# print(x)

# # Do a search that will return a Match Object
# x = re.search('ai', txt)
# print(x)

# #Search for an upper case "S" character in the beginning of a word, 
# and print its position:
# x = re.search(r"\bS\w+", txt)
# print(x.span())

#Print the string passed into the function:
# x = re.search(r"\bS\w+", txt)
# print(x.string)

#The regular expression looks for any words that starts with an upper case "S"
#x = re.search(r"\bS\w+", txt)
# print(x.group())