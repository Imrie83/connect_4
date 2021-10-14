import pygame
import numpy as np

ROW_COUNT = 6
COL_COUNT = 7
def creat_board():
    board = np.zeros((6, 7))
    return board

board = creat_board()
turn = 0
game_over = False

def drop_piece(board, row, column, piece):
    board[row][column] = piece

def is_valid_location(board, column):
    return board[5][column] == 0

def get_next_open_row(board, column):
    for r in range(ROW_COUNT):
        if board[r][column] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        column = int(input("Player 1 make your move (0 - 6): "))
        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 1)
        else:


    # Ask for Player 2 Input
    else:
        column = int(input("Player 2 m ake your move (0 - 6): "))
        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 2)


    turn += 1
    turn = turn%2
    print_board(board)
