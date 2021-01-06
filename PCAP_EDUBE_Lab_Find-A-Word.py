"""
PCAP Path_EDUBE: Section 5.1.11.10: Lab_Find a word
Scenario
Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of
 any characters.

Your task is to write a program which answers the following question: are the characters comprising the first string
hidden inside the second string?

For example:
    if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
    if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)

    Hints:

        you should use the two-argument variants of the pos() functions inside your code;
        don't worry about case sensitivity.
"""
## Ask the user to enter the two texts
text1=input('Please Enter first string')
text2=input('Please Enter the second strings, where to check if characters comprising the first string are hidden inside')
###
#Convert the caracters from Captial to lower cases for both texts:
##
text1=text1.lower()
text2=text2.lower()
#########
# Start the check
#########
ix=0  # ix is  the vairable for the string index
word=''
for ch1 in text1:
    c=text2.find(ch1,ix)
    if c!=-1:
        ix=c
        word+=ch1
    else:
        break
if word== text1:
    print('yes')
else:
    print('No')
