"""
Module to enable a TIC-TAC-TOE game

"""

import random as rd

def drawBoard(board):
    '''
    Draw the current board state in the console, indicating rows (1, 2, 3) and
    columns (a, b, c).

    Parameters:
        board (list): A list of lists defining the 3x3 board state. Each cell
                      can contain one of the following characters: ' ', 'X', 'O'

    Returns:
        None
    '''
    line = '     +---+---+---+'

    # Header
    print('\n')
    print('       a   b   c  ')

    # Rows
    print(line)
    for i, row in enumerate(board):
        print('   {0} | {1[0]} | {1[1]} | {1[2]} |'.format(1 + i, row))
        print(line)

    print('\n')

def checkBoard(board):
    count = 0
    global end
    end = False
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            print(f'{board[i][0]} wins!')
            count += 1
            end = True
            break
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            print(f'{board[0][i]} wins!')
            count += 1
            end = True
            break

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        print(f'{board[0][0]} wins!')
        count += 1
        end = True
    if board[0][2] == board[1][1] == board[2][0] != ' ' and count == 0:
        print(f'{board[0][2]} wins!')
        count += 1
        end = True

    for row in board:
        if ' ' in row and end != True:
            print('The game continues')
            break
        else:
            print('Game over')
            break

    if count == 0 and ' ' not in row:
        print('Draw')
        end = True

def playerMove(board, player, row, column):
    try:
        row = row - 1
        if column == 'a' or column == 'b' or column == 'c':
            column = ord(column) - 97
        # Check if the cell is occupied
        if board[row][column] != ' ':
            print("Occupied cell. Enter a valid move.")
            return False

        # Check if coordinates are within the board range
        if row < 0 or row > 2 or column < 0 or column > 2:
            print("Nonexistent cell. Enter a valid move.")
            return False

        # If no errors, record the move
        board[row][column] = player
        return True
    except IndexError:
        print("Error: Enter a valid move.")
        return False

def computerMove(board):
    possible_moves = []
    count = 0
    global COMPUTER
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                possible_moves.append(str(i) + str(j))
                count += 1
    if count == 8:
        for i in range(3):
            for j in range(3):
                if board[i][j] != ' ':
                    if board[i][j] == 'X':
                        COMPUTER = 'O'
                    if board[i][j] == 'O':
                        COMPUTER = 'X'
    if count == 9:
        choice = rd.randint(0, 1)
        if choice == 0:
            COMPUTER = 'O'
        else:
            COMPUTER = 'X'

    possible_moves = []
    if count != 0:
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    possible_moves.append(str(i) + str(j))
                    count += 1
        move = list(possible_moves[rd.randint(0, len(possible_moves) - 1)])
        row = int(move[0])
        col = int(move[1])
        board[row][col] = COMPUTER

def newGame():
    M = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    computerMove(M)
    drawBoard(M)
    checkBoard(M)
    count = 0
    coordinates = list(input('Enter the position you want to fill (format: number-letter): '))
    pos1 = int(coordinates[0])
    pos2 = coordinates[1]
    for i in range(3):
        for j in range(3):
            if M[i][j] != ' ':
                if M[i][j] == 'X':
                    player = 'O'
                if M[i][j] == 'O':
                    player = 'X'
    while end != True:
        playerMove(M, player, pos1, pos2)
        drawBoard(M)
        checkBoard(M)
        if end != True:
            computerMove(M)
            drawBoard(M)
            checkBoard(M)
        if end != True:
            coordinates = list(input('Enter the position you want to fill (format: number-letter): '))
            pos1 = int(coordinates[0])
            pos2 = coordinates[1]
        for i in range(3):
            for j in range(3):
                if M[i][j] == ' ':
                    count += 1
        if count == 0:
            break