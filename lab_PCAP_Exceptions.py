def readint(prompt, min, max):
    try:
        n=int(input(prompt))
        if n<=max and n>= min:
            return n
        else:
            print('Error: the value is not within the permitted value (',min,'..',max,')')
            readint(prompt, min, max)
    except ValueError:
            print('Error: wrong Input')
            readint(prompt, min, max)

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)