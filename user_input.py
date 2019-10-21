"""Handles user input"""

import string

from board import get_x_coordinate, get_y_coordinate, create_solution_board


def get_solution_board():
    """Asks for dimensions and return a solution board"""
    valid = False
    height_exists = False
    while not valid:
        if not height_exists:
            height = input('Número de casillas de alto (6): ')
            if height and not height.isdigit():
                print('ERROR: Argumento no válido')
                continue
            else:
                height_exists = True
        width = input('Número de casillas de ancho (6): ')

        if width and not width.isdigit():
            print('ERROR: Argumento no válido')
            continue
        if width and int(width) >= 26:
            print('El ancho debe ser menor a 26')
            continue

        if not width:
            width = 6
        if not height:
            height = 6
        width = int(width)
        height = int(height)
        try:
            board = create_solution_board(width, height)
        except ValueError:
            print('El número de casillas en total no es múltiplo de dos.\n')
            height_exists = False
            continue
        valid = True
    return board


def ask_for_coordinates(board):
    """Asks for coordinates"""
    row_limit = len(board)
    column_limit = string.ascii_uppercase[len(board[0]) - 1]
    while True:
        print('\nPrimera casilla:')
        while True:
            y1 = input('Ingresa una fila (1-{}): '.format(row_limit))
            x1 = input('Ingresa una columna (A-{}): '.format(column_limit))
            x1 = get_x_coordinate(x1, board)
            y1 = get_y_coordinate(y1, board)
            if x1 >= 0 and y1 >= 0:
                break
            else:
                print('\nCoordenada no válida')

        print('\nSegunda casilla:')
        while True:
            y2 = input('Ingresa una fila (1-{}): '.format(row_limit))
            x2 = input('Ingresa una columna (A-{}): '.format(column_limit))
            x2 = get_x_coordinate(x2, board)
            y2 = get_y_coordinate(y2, board)
            if x2 >= 0 and y2 >= 0:
                break
            else:
                print('\nCoordenada no válida')

        if (x1, y1) == (x2, y2):
            print('\nERROR: Las coordenadas son iguales')
        else:
            break
    return (x1, y1), (x2, y2)
