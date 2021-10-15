import pygame
import numpy as np

ROW_COUNT = 6
COL_COUNT = 7


def creat_board():
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board


board = creat_board()
turn = 0
game_over = False


def drop_piece(board, row, column, piece):
    board[row][column] = piece


def is_valid_location(board, column):
    return board[ROW_COUNT-1][column] == 0


def get_next_open_row(board, column):
    for r in range(ROW_COUNT):
        if board[r][column] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # horizontal location check
    for c in range(COL_COUNT- 3 ):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # vertical location check
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # positive slope check
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece \
                and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # positive slope check
    for c in range(COL_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece \
                and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True


while not game_over:

    if winning_move(board, 1):
        print("Player 1 wins!")
        break
    elif winning_move(board, 2):
        print("Player 2 wins!")
        break

    # Ask for Player 1 Input
    if turn == 0:
        column = int(input("Player 1 make your move (0 - 6): "))
        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 1)

        else:
            while not is_valid_location(board, column):
                column = int(input("Not a valid choice, select again (0 - 6): "))
                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 1)

    # Ask for Player 2 Input
    else:
        column = int(input("Player 2 m ake your move (0 - 6): "))
        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 2)
        else:
            while not is_valid_location(board, column):
                column = int(input("Not a valid choice, select again (0 - 6): "))
                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 2)

    turn += 1
    turn = turn%2
    print_board(board)
