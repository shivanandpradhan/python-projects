#q7
#regular expression for ba*b

#  importing regular expression
import re

# given pattern  is ba*b
#defining a pattern

patt = input("Enter regular expression : \n")

#defining a pattern
pattern = re.compile(patt)

# getting an input from the string
str = input("\tEnter a String : ")

# finding all matches related to pattern in string
matches = re.findall(pattern, str)

# displaying all the matched string.
matchList = []
for match in matches : 
    matchList.append(match)

if (len(matchList) == 0):
    print("Invalid String for given re :",patt)

else : 
    print("String is accepted.")
    print("Matched Strings are : ")
    print(matchList)
