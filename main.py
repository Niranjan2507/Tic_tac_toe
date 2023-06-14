import random
board = ["_","_","_",
        "_","_","_",
        "_","_","_"]
currentplayer = "X"
winner = None
gamerunning = True


def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print('-----')
    print(board[3] + "|" + board[4] + "|" + board[5])
    print('-----')
    print(board[6] + "|" + board[7] + "|" + board[8])


def playerInput(board):
    inp = int(input('Enter the number: '))
    if inp >= 1 and inp <= 9 and board[inp-1] == '_':
        board[inp-1] = currentplayer
    else:
        print('the number is occupied')


def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '_':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '_':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '_':
        winner = board[6]
        return True


def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '_':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '_':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '_':
        winner = board[2]
        return True


def checkdia(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '_':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '_':
        winner = board[2]
        return True


def checkTie(board):
    global gamerunning
    if '_' not in board:
        printBoard(board)
        print('it is a tie')
        gamerunning = False


def checkwin():
    if checkdia(board) or checkRow(board) or checkHorizontal(board):
        print(f"winner is {winner}")
        gamerunning=False
        exit()


def switchPlayer():
    global currentplayer
    if currentplayer == 'X':
        currentplayer = 'O'
    else:
        currentplayer = 'X'

def computer(board):
    while currentplayer == 'O':
        position = random.randint(0, 8)
        if board[position]=="_":
            board[position]="O"
            switchPlayer()



while gamerunning:
    printBoard(board)
    playerInput(board)
    checkwin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkwin()
    checkTie(board)






