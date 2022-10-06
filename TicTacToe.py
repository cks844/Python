import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
pl1='X'
pl2='O'
def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,'won')
            return True
    return False
def check_cols(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[c][r]==symbol:
                count=count+1
        if count==3:
            print(symbol,'won')
            return True
    return False
def check_diagonals(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    return False

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol):
        
def place(symbol):
    while(1):
    print(numpy.matrix(board))
    row=int(input("Enter row position(1/2/3):"))
    col=int(input("Enter row position(1/2/3):"))
    if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
        break
    else:
        print("Invalid input")
    board[row-1][col-1]=symbol
    
define play():
    for turn in range(9):
        if turn%2==0:
            print('X turn')
            place(pl1)
            if won(pl1):
                break
        else:
            print('O turn')
            place(pl2)
            if won(pl2):
                break
        if not (won(pl1)) and not(won(pl2)):
            print("Draw")
play()
