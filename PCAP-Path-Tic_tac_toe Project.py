def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', board[0][0], '  |  ', board[0][1], '  |  ', board[0][2], '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', board[1][0], '  |  ', board[1][1], '  |  ', board[1][2], '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', board[2][0], '  |  ', board[2][1], '  |  ', board[2][2], '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')


def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move,
# checks the input and updates the board according to the user's decision
#
#    global board
    Pos = int (input('Give the position of your Move < Number  in the range : 1 to 9>'))
    if Pos < 1 or Pos >9:
        print(' Sorry, the number your Porvided is out of Range,Give  again the position of your Move < Number  in the range : 1 to 9>')
        EnterMove(board)
    free = MakeListOfFreeFields(board)
    print (dict[Pos])
    (i,j)=dict[Pos]
    if (i,j) in free:
        board[i][j]='O'
    else:
        print('the cell is already taken, choose another cell')
        EnterMove(board)
    return board

def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares;
# the list consists of tuples, while each tuple is a pair of row and column numbers
#    global board
    freeSqr=[]
    for i in range (3):
        for j in range (3):
            if board [i][j] =='X' or board [i][j] =='O':
                continue
            freeSqr.append ((i,j))
    #print(freeSqr)
    return freeSqr


def VictoryFor(board, sign):
    #
    # the function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    #++
    Gameover=False
    # verifier la diagonal (0,0),(1,1),(2,2)
    X = 0
    O = 0
    for i in range (3):
        if board[i][i]== "X":
            X+=1
        if board[i][i]== "O":
            O+=1
    if (X==3 ) or (O==3):
        Gameover=True
    if Gameover==False:
        X = 0
        O = 0
    # verifier la diagonal (0,2),(1,1),(2,0):
        for i in range (3):
            if board[i][2-i] == "X":
                X += 1
            if board[i][2-i] == "O":
                O += 1
    if X == 3 or O == 3:
        Gameover = True
    ## check the three row
    if Gameover==False:
        for i in range(3):
            X = 0
            O = 0
            for j in range(3):
                if board[i][j] == "X":
                    X += 1
                if board[i][j] == "O":
                    O += 1
            if X == 3 or O == 3:
                Gameover = True
                break
    if Gameover == False:
        # Check the 3 columns:
        for i in range (3):
            X=0
            O=0
            for j in range (3):
                if board[j][i] == "X":
                    X += 1
                if board[j][i] == "O":
                    O += 1
            if X == 3 or O == 3:
                Gameover = True
                break
    if Gameover == True:
        if X==3:
            sign='X'
        if O==3:
            sign='O'
    else:
        sign='N'
    #print(sign)
    return sign


def DrawMove(board):
#
# the function draws the computer's move and updates the board
#
#    global board
    CompMv=randrange(1,10)
    free = MakeListOfFreeFields(board)
    #print(free)
    #for (i,j) in free:
    (i, j) = dict[CompMv]
    if (i, j) in free:
        board[i][j] = "X"
    else:
        print(' the cell is already taken')
        DrawMove(board)
    #DisplayBoard(board)
    return board

######> define  the board for the first time:
from random import randrange
board =[]
num=0
for i in range (3):
    col=[]
    for j in range (3):
        if (j == 1) and (i == 1):
             col.append('X')
             num += 1
        else:
            num +=1
            col.append(num)
    board.append(col)
# define a dictionnary with (key: values ) as ('[1-10]: saquare postion in array)
num=1
dict={}
for i in range (3):
    for j in range (3):
        dict.update({num:(i,j)})
        num+=1
# Display the Board layount
DisplayBoard(board)
sign=""
while True:
    # PLayer to enter the move1
    board=EnterMove(board)
    sign = VictoryFor(board, sign)

    if sign =="X" or sign =="O":
        break
    # Computer to enter the move:
    board=DrawMove (board)
    DisplayBoard(board)
    # Check victory
    sign=VictoryFor(board,sign)
    if sign =="X" or sign =="O":
        break
    free=MakeListOfFreeFields(board)
    if len(free)==0:
        print('Game Over, No more empty cells and  Neither Players Win,')
        break
DisplayBoard(board)
if sign=='X':
     print(' Game Over:::You Lost')
elif sign =='O':
         print ('Game Over::: You Won')






