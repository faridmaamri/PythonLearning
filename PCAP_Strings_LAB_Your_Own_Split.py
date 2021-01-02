def mysplit(strng):
    list = []
    ix = 0
    if strng.isspace():
        return list
    for i in range(len(strng)):
        caract = strng[i]
        if caract.isspace():
            word = strng[ix:i]
            if len(word) ==0:
                ix=i+1
                continue
            ix = i + 1
            if word.isspace():
                continue
            list.append(word)
    word=strng[ix:]
    if len(word)!=0:
        list.append(word)
    return list


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
#print(mysplit("abc    "))
print(mysplit(""))