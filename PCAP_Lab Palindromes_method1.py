"""
EDUB_PCAP path: LAB 5.1.11.7 Plaindromes
Do you know what a palindrome is?

It's a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.

Your task is to write a program which:

asks the user for some text;
checks whether the entered text is a palindrome, and prints result.
Note:

    - assume that an empty string isn't a palindrome;
    - treat upper- and lower-case letters as equal;
    - spaces are not taken into account during the check - treat them as non-existent;
    there are more than a few correct solutions - try to find more than one.

"""
### Ask the user to enter the text  or sentence
text=input('Please enter the text to check : ')
##remove spaces and convert  all caracters to lower case
string=text.replace(' ','')
string=string.lower()
revtext=''
for i in range (1,len(string)+1):
    revtext+=string[-i]
if string == revtext:
    print( 'it\'s a palindrome')
else:
    print('it\'s not a palindrome')
