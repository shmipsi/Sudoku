
def validate_format(sudoku):
    if not isinstance(sudoku, list) or len(sudoku) != 9:
        return 0
    return 1

def validate_negative(sudoku):
    for row in sudoku:
        for value in row:
            if value < 0:
                return 0
    return 1

# Validating sums
def validate_row_sums(sudoku):
    for row in sudoku:
        if sum(row) != 45:
            return 0
    return 1

def validate_column_sums(sudoku):
    for col in range(9):
        col_sum = sum(sudoku[row][col] for row in range(9))
        if col_sum != 45:
            return 0
    return 1

def validate_box_sums(sudoku):
    for box_row in range(3):
        for box_col in range(3):
            box_sum = 0
            for row in range(box_row * 3, box_row * 3 + 3):
                for col in range(box_col * 3, box_col * 3 + 3):
                    box_sum += sudoku[row][col]
            if box_sum != 45:
                return 0
    return 1

# main validation function(call it)
def validate_sudoku(sudoku):
    format_valid = validate_format(sudoku)
    negative_valid = validate_negative(sudoku)

    #sums
    row_sum = validate_row_sums(sudoku)
    column_sum = validate_column_sums(sudoku)
    box_sum = validate_box_sums(sudoku)

    return (format_valid, negative_valid, row_sum, column_sum, box_sum)
