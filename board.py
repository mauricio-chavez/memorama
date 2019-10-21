"""Board module"""

import copy
import math
import random
import string


def create_solution_board(width=6, height=6):
    """Randomly generates a new board
    with width by height size
    """
    if type(width) != int or type(height) != int:
        raise TypeError('Arguments must be int type')

    boxes = width * height

    if boxes % 2 != 0:
        raise ValueError('Number of boxes is not multiple of two')

    numbers = list(range(1,  boxes // 2 + 1))
    numbers = numbers + numbers
    random.shuffle(numbers)

    board = []

    for index in range(height):
        board.append([])
        for _ in range(width):
            random_number = numbers.pop()
            board[index].append(random_number)
        board[index] = board[index]
    return board


def start_board(solution_board):
    """Generates an empty board from a solution board"""
    empty_board = copy.deepcopy(solution_board)
    for row in empty_board:
        for index in range(len(row)):
            row[index] = '-'

    return empty_board


def format_board(board):
    """Returns a printable board"""
    fboard = ''
    width = len(board[0])
    height = len(board)
    cards = (width * height) // 2
    letters = string.ascii_uppercase[:width]

    if width > len(letters):
        raise ValueError('Board width is greater than ' + len(letters))

    number_space = int(math.log10(height)) + 2
    number_format = '{{:^{}}}'.format(number_space)
    max_digits = int(math.log10(cards)) + 2
    box_format = '|{{:^{}}}'.format(max_digits)

    letter_row = ' ' * number_space
    for letter in letters:
        letter_row += box_format.format(letter)
    letter_row += '\n'

    for row in range(height):
        fboard += number_format.format(row + 1)
        for number in board[row]:
            fboard += box_format.format(number)
        fboard += '\n'

    return letter_row + fboard


def get_x_coordinate(x, board):
    """Returns input as index in x coordinate"""
    width = len(board[0])
    letters = string.ascii_lowercase[:width]

    index = letters.find(x.strip().lower())

    if index >= 0:
        return index
    else:
        return -1


def get_y_coordinate(y, board):
    """Returns input as index in y coordinate"""
    try:
        y = int(y)
    except ValueError:
        return -1
    height = len(board)
    y -= 1

    if y >= 0 and y < height:
        return y
    else:
        return -1
