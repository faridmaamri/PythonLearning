"""
PCAP EDUBE path: Section 6.1.9.15 LAB: Character frequency histogram
 text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

asks the user for the input file's name;
reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
prints a simple histogram in alphabetical order (only non-zero counts should be presented)
Create a test file for the code, and check if your histogram contains valid results.

Assuming that the test file contains just one line filled with:

aBc

the expected output should look as follows:
a -> 1
b -> 1
c -> 1

Tip:

We think that a dictionary is a perfect data collection medium for storing the counts. The letters may be keys while the counters can be values.

"""
def Countalpha(Line,count):
    Line=Line.lower()
    for ch in Line:
        if ch.isalpha():
            count[ch]+=1
        else:
            continue
    return count

from os import strerror
#Ask the user to enter the file name
file=input('PLease provide the file name')
# Construct the dictionar fro storing the value of each alphabetic caracter count:
count={}
for i in range (26):
    count[chr(ord('a')+i)]=0

# open the file
try:
    src=open(file,'rt')
except FileNotFoundError as err:
    print(' File Location Error:',err)
except IOError as e:
    print('Cannot open the file:',strerr(e.errno))
## Read Each line from the  file and count the caracters
Line=src.readline()
## count the number of alphabetic caracters in each text line
while Line!='':
    Countalpha(Line,count)
    Line = src.readline()
### print the result:
src.close()
for key in count.keys():
    if count[key]!=0:
        print(key,'->',count[key])






