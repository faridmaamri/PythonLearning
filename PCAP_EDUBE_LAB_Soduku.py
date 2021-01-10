"""
PCAP Path_EDUBE_ Section 5.1.11.11: Lab: Soduku
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

    -each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
    -each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
    -each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
    - If you need more details, you can find them here.

Your task is to write a program which:

reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.
"""
## Define a function that Checks eah row or the soduku board
def checkRow (table,n):
    for i in range (n):
        st = []
        for j in range (n):
            if table[i][j] in st:
                return False
            st.append(table[i][j])
    return True

## Define a function that Checks eah column or the soduku board
def checkCol (table, n):
    for i in range (n):
        st = []
        for j in range (n):
            if table[j][i] in st:
                return False
            st.append(table[j][i])
    return True
def validSubsqr (table,start,end):
    st=[]
    for i in range (start,end):
        for j in range (start,end):
            if table[i][j] in st:
                return False
            st.append(table[i][j])
    return True

#### Define a function that Checks eah 3x3 sub-square  of the soduku board
    ## determine the value of endindex of  3 subsquares
def checksubsqr (table,n):
    strt=[]
    endix=[]
    for i in range (n//3):
        strt.append(i*3)
        endix.insert(0,n-3*i)
    print(strt,'\n',endix)
    #strt=[0,3,6]
    #endix=[3,6,9]
    for i in range (3):
        start=strt[i]
        end=endix[i]
        v=validSubsqr(table,start,end)
        if v==False:
            return False
    return True

##Ask th User to Enter the  dimension of the the Soduku table:
n=int(input("Please enter the dimension of the table, for example if the table diemnsion is \"9x9\"==> <enter 9 >:  "))
##Ask th User to Enter the  rows of the soduku table:
table=[]
for i in range (n):
    print("""PLease enter the "ROW" number""",i+1,':')
    row=input()
    ROW=list(row)
    table.append(ROW)
## Start the Checks of the Soduku tables
if checkRow(table,n) and checkCol(table,n) and checksubsqr (table,n):
    print('Yes')
else:
    print('No')
