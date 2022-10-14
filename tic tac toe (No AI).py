import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentplayer = "X"
winner = None
gameRunning = True

# Setting up the board


def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# adding the mechanics to put something on the board


def PlayerInput(board):
    user_input = int(input("Pick a board: "))
    if user_input >= 1 and user_input <= 9 and board[user_input - 1] == "-":
        board[user_input - 1] = currentplayer
    elif user_input < 1 or user_input > 9:
        print("please pick another board")
    else:
        print("That spot is already taken")

# Checking for wins and ties


def CheckHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner = board[4]
        return True


def CheckRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[5]
        return True


def CheckDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[0]
        return True


def CheckTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False


def checkWin():
    global gameRunning
    if CheckDiagonal(board) or CheckHorizontal(board) or CheckRow(board):
        print(f"The weiner is {winner}")
        gameRunning = False

# switch player


def switchPlayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"
# computer opponent


def computer(board):
    while currentplayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gameRunning:
    printBoard(board)
    PlayerInput(board)
    checkWin()
    CheckTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    CheckTie(board)
