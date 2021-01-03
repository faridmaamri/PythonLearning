"""
 this program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:

  # ### ### # # ### ### ### ### ### ###
  #   #   # # # #   #     # # # # # # #
  # ### ### ### ### ###   # ### ### # #
  # #     #   #   # # #   # # #   # # #
  # ### ###   # ### ###   # ### ### ###
"""
## def a function to print the pattern
def displayLed (number):
    for i in range (5):
        for k in range (len(number)) :
            d=number[k]
            print(d[i], end='  ')
        print()

def CheckNumber (n):
    if n == '0':
        return 0
    if n == '1':
        return 1
    if n =='2':
        return 2
    if n=='3':
        return 3
    if n=='4':
        return 4
    if n=='5':
        return 5
    if n=='6':
        return 6
    if n=='7':
        return 7
    if n=='8':
        return 8
    if n=='9':
        return 9

### Construct a list containing  0 to 9 digit patterns
zero=['# # #','#   #','#   #','#   #','# # #']
one=['  #','  #','  #','  #','  #']
two=['# # #','    #','# # #','#    ','# # #']
three=['# # #','    #','# # #','    #','# # #']
four=['#   #','#   #','# # #','    #','    #']
five=['# # #','#    ','# # #','    #','# # #']
six=['# # #','#    ','# # #','#   #','# # #']
seven=['# # #','    #','    #','    #','    #','    #']
eight=['# # #','#   #','# # #','#   #','# # #']
nine=['# # #','#   #','# # #','    #','# # #']
digit=[zero,one,two,three,four,five,six,seven,eight,nine]
##
# Create a list named numbers that contained the displat pattern of the entered digits
number=[]
# Ask the User to enter a number
num=input('PLease enter a digit to display')
## check for the number that are entered by the user and appends the number list with the pattern
# of each digit of the entered number
for i in  range (len(num)):
    ix=CheckNumber(num[i])
    number.append(digit[ix])
displayLed(number)


