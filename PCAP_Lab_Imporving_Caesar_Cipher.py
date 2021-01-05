"""
Edube (Python Institute) course_PCAP path_Lab Improving Caesar Cipher
course section title:5.1.11.6 LAB:Improving the Caesar Cipher
 this program  Improves the Caesar Cipher and allows the shifted value to come from the range 1..25 inclusive.

 Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case)
 and all non-alphabetical characters should remain untouched.

 """
# Ask the User to Enter the text

text=input(' Please, enter the text to encrypt using Caesar Cipher method')

#Ask the user to enter  character shift value
try:
    shift=int(input('PLease, Enter the shift value in the range <1 - 25 >'))
except ValueError:
    print(' the entered value is not number ')
    shift=int(input('PLease, Enter the shift value in the range <1 - 25 >'))
# start the encryption
textcrypt=''
for i in range (len(text)):
    # check for Capital Letters and encrypt them
    if ord(text[i])>= ord('A') and ord(text[i])<=ord('Z'):
        ('print capital ')
        c=ord(text[i])+ shift
        print(c)
        if c > ord('Z'):
            c= (c-ord('Z'))+ord('A')-1
        ch=chr(c)
        textcrypt+=ch
        print('encypted character is',textcrypt)
    elif ord(text[i])>=ord('a') and ord(text[i])<=ord('z'):
        ('print capital ')
        c=ord(text[i])+ shift
        if c > ord('z'):
            c = (c - ord('z')) + ord('a') - 1
        ch=chr(c)
        textcrypt += ch
    else:
        textcrypt +=text[i]
print(textcrypt)
