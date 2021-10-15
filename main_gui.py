import pygame
import sys
import math
import numpy as np

ROW_COUNT = 6
COL_COUNT = 7
BLUE = (19, 25, 189)
BLACK = (0, 0, 0)
DARK_GRAY = (54, 54, 54)
RED = (133, 5, 16)
GREEN = (26, 133, 5)


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
    for c in range(COL_COUNT - 3):
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


def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK,
                               (c * SQUARE_SIZE + (SQUARE_SIZE / 2), r * SQUARE_SIZE + (SQUARE_SIZE * 1.5)),
                               CIRCLE_SMALL / 2)
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED,
                                   (column * SQUARE_SIZE + (SQUARE_SIZE / 2), height + SQUARE_SIZE - (row * SQUARE_SIZE + (SQUARE_SIZE * 1.5))),
                                   CIRCLE_SMALL / 2)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, GREEN,
                                   (column * SQUARE_SIZE + (SQUARE_SIZE / 2), height + SQUARE_SIZE - (row * SQUARE_SIZE + (SQUARE_SIZE * 1.5))),
                                   CIRCLE_SMALL / 2)
    pygame.display.update()

pygame.init()

SQUARE_SIZE = 100
CIRCLE_LARGE = 94
CIRCLE_SMALL = 86
width = COL_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE
size = (width, height)

pygame.display.set_caption("Connect Four")
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos[0])
            # 'naive' way to get a position
            # if event.pos[0] < 100:
            #     column = 0
            # elif event.pos[0] >= 100 and event.pos[0] < 200:
            #     column = 1
            # elif event.pos[0] >= 200 and event.pos[0] < 300:
            #     column = 2
            # elif event.pos[0] >= 300 and event.pos[0] < 400:
            #     column = 3
            # elif event.pos[0] >= 400 and event.pos[0] < 500:
            #     column = 4
            # elif event.pos[0] >= 500 and event.pos[0] < 600:
            #     column = 5
            # elif event.pos[0] >= 600 and event.pos[0] < 700:
            #     column = 6

            # Ask for Player 1 Input
            if turn == 0:
                column = int(math.floor(event.pos[0] / SQUARE_SIZE))
                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 1)
                else:
                    while not is_valid_location(board, column):
                        column = int(math.floor(event.pos[0] / SQUARE_SIZE))
                        if is_valid_location(board, column):
                            row = get_next_open_row(board, column)
                            drop_piece(board, row, column, 1)

                if winning_move(board, 1):
                    print("Player 1 wins!")


            # Ask for Player 2 Input
            else:
                column = int(math.floor(event.pos[0] / SQUARE_SIZE))
                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 2)


                else:
                    while not is_valid_location(board, column):
                        column = int(math.floor(event.pos[0] / SQUARE_SIZE))
                        if is_valid_location(board, column):
                            row = get_next_open_row(board, column)
                            drop_piece(board, row, column, 2)

                if winning_move(board, 2):
                    print("Player 2 wins!")


            turn += 1
            turn = turn % 2
            print_board(board)
            draw_board(board)
