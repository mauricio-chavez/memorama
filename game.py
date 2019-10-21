"""Game dynamics"""

from board import format_board


def turn(first, second, board, solution_board):
    """Fills board if user find out a pair"""
    first_box = solution_board[first[1]][first[0]]
    second_box = solution_board[second[1]][second[0]]

    board[first[1]][first[0]] = first_box
    board[second[1]][second[0]] = second_box
    fboard = format_board(board)
    print('\n' + fboard)

    if first_box == second_box:
        print('\n¡Has encontrado un par!')
        return [first, second]
    else:
        print('\n¡Has fallado!')
        board[first[1]][first[0]] = '-'
        board[second[1]][second[0]] = '-'
