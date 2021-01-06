"""
PCAP PAth _EDUBE
section: 5.1.11.9: Lab: Digit of Life
Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple - you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:

1 January 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 is the digit we searched for and found.

Your task is to write a program which:

asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)
outputs the Digit of Life for the date.
"""

# define a function that perform the sum of all the digits of the date of birth
def SumBirth(date):
    sum=0
    for i in range (len(date)):
        sum+=int(date[i])
    return sum

## ask the user to enter the date
date= input(' please en a date in digits in the the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY')
sum='00'
while len(str(sum)) >1:
    try:
        sum=SumBirth(date)
        date=str(sum)
    except ValueError:
        print(' << ERROR >> : at least one entered character is not a digit')
        date = input(' please en a date in digits in the the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY')

print(sum)
