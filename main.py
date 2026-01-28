import terminal_interface
import sudoku_validation
import sudoku_solver

# test arrays
b2 = [
    [8, 9, 6, 2, 4, 3, 7, 5, 1],
    [5, 7, 3, 9, 6, 1, 8, 4, 2],
    [2, 4, 1, 5, 7, 8, 9, 3, 6],
    [1, 6, 2, 8, 3, 9, 4, 7, 5],
    [4, 5, 8, 1, 2, 7, 3, 6, 9],
    [7, 3, 9, 4, 5, 6, 1, 2, 8],
    [6, 1, 5, 7, 8, 4, 2, 9, 3],
    [9, 2, 7, 3, 1, 5, 6, 8, 4],
    [3, 8, 4, 6, 9, 2, 5, 1, 7]
    ]

b3 = [
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    [5, 7, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 5, 7, 8, 9, 3, 6],
    [0, 6, 2, 0, 3, 9, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 3, 0, 9],
    [0, 0, 9, 0, 0, 0, 0, 2, 8],
    [0, 0, 5, 7, 0, 4, 2, 9, 0],
    [0, 0, 7, 0, 1, 0, 6, 0, 0],
    [0, 8, 0, 6, 9, 0, 0, 0, 7]
    ]


terminal_interface.print_array(b2)
terminal_interface.print_array(b3)
print(type(b2))
sudoku_validation.validate_sudoku(b2)

