"""Main script"""

from board import format_board, start_board
from game import turn
from user_input import get_solution_board, ask_for_coordinates


try:
    solution_board = get_solution_board()
    board = start_board(solution_board)

    width = len(board[0])
    height = len(board)
    boxes = width * height

    coordinates = []
    playing = True

    print('\n' + format_board(board))
    while playing:
        first, second = ask_for_coordinates(board)
        if first in coordinates or second in coordinates:
            print('\nYa has volteado estas casillas.')
            continue
        
        tuples = turn(first, second, board, solution_board)
        if tuples:
            coordinates.append(tuples[0])
            coordinates.append(tuples[1])

            if len(coordinates) == boxes:
                print('\n¡HAS GANADO!')
                break

except KeyboardInterrupt:
    print('\nJuego terminado por el usuario.')
