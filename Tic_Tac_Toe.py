# Tic Tac Toe
# Main functions
import random
board = [' 'for x in range(10)]

def insertBoard(letter, pos):
    global board
    board[pos] = letter
def spaceIsFree(pos): # Checks if space is free
    return board[pos] == ' '
def printBoard():
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
def isWinner(bo,le): # Checks if someone wins
    return (bo[7] == le and bo[8] == le and bo[9] == le) or \
    (bo[4] == le and bo[5] == le and bo[6] == le) or \
    (bo[1] == le and bo[2] == le and bo[3] == le) or \
    (bo[1] == le and bo[4] == le and bo[7] == le) or \
    (bo[2] == le and bo[5] == le and bo[8] == le) or \
    (bo[3] == le and bo[6] == le and bo[9] == le) or \
    (bo[1] == le and bo[5] == le and bo[9] == le) or \
    (bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():
    run = True
    while run:
        move = input('Select a position from 1-9 to place an "x":')
        try:
            move = int(move)
            if 0 < move < 10:
                if spaceIsFree(move):
                    run = False
                    insertBoard('X', move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('Please type a number between 1-9')
        except:
            print('Please type a number')
def compMove():
    possible_moves = [x for x, letter in enumerate(board)if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if isWinner(board_copy, let):
                move = i
                return move
    corners_open = []
    for i in possible_moves:
        if i in (1,3,7,9):
            corners_open.append(i)
    if len(corners_open) > 0:
        move = selectRandom((corners_open))
        return move
    if 5 in possible_moves:
        move = 5
        return move
    edges_open = []
    for i in possible_moves:
        if i in (2,4,6,8):
            edges_open.append(i)
    if len(edges_open) > 0:
        move = selectRandom((edges_open))
        return move

def selectRandom(li):
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print("Tic Tac Toe!")
    printBoard()

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print('Sorry, the computer has won!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertBoard('O', move)
                print('The computer placed an "O" in position, ' + str(move) + ':')
                printBoard()
        else:
            print('The player has won! Good Job!')
            break
    if isBoardFull(board):
        print("Tie Game!")


main()
again = input("Would you like to play again? Y/N")
while True:
    if again == "Y" or "yes":
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break
