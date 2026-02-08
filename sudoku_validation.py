
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

# Validating unique values
#**set** - list that stores only unique values, order doesn't matter.
def validate_unique_boxes(sudoku):
    for box_row in range(3):
        for box_col in range(3):
            seen = set()
            for row in range(box_row * 3, box_row * 3 + 3):
                for col in range(box_col * 3, box_col * 3 + 3):
                    value = sudoku[row][col]
                    if value != 0:
                        if value in seen:
                            return 0
                        seen.add(value)
    return 1

def validate_unique_rows(sudoku):
    for row in sudoku:
        seen = set()
        for value in row:
            if value != 0:
                if value in seen:
                    return 0
                seen.add(value)
    return 1

def validate_unique_columns(sudoku):
    for col in range(9):
        seen = set()
        for row in range(9):
            value = sudoku[row][col]
            if value != 0:
                if value in seen:
                    return 0
                seen.add(value)
    return 1

def validate_unique_box(sudoku, box_row, box_col):
    seen = set()
    for row in range(box_row * 3, box_row * 3 + 3):
        for col in range(box_col * 3, box_col * 3 + 3):
            value = sudoku[row][col]
            if value != 0:
                if value in seen:
                    return 0
                seen.add(value)
    return 1

def validate_unique_row(sudoku, row_index):
    seen = set()
    for value in sudoku[row_index]:
        if value != 0:
            if value in seen:
                return 0
            seen.add(value)
    return 1

def validate_unique_column(sudoku, col_index):
    seen = set()
    for row in range(9):
        value = sudoku[row][col_index]
        if value != 0:
            if value in seen:
                return 0
            seen.add(value)
    return 1

#main functions(call it)
def validate_unique_values(sudoku):
    boxes = validate_unique_boxes(sudoku)
    rows = validate_unique_rows(sudoku)
    cols = validate_unique_columns(sudoku)
    return (rows, cols, boxes)

def validate_sudoku(sudoku):
    format_valid = validate_format(sudoku)
    negative_valid = validate_negative(sudoku)

    #sums
    row_sum = validate_row_sums(sudoku)
    column_sum = validate_column_sums(sudoku)
    box_sum = validate_box_sums(sudoku)

    return (format_valid, negative_valid, row_sum, column_sum, box_sum)

def validate_all(sudoku):
    format_valid, negative_valid, row_sum, column_sum, box_sum = validate_sudoku(sudoku)
    row_unique, col_unique, box_unique = validate_unique_values(sudoku)
    if all([format_valid, negative_valid, row_sum, column_sum, box_sum, row_unique, col_unique, box_unique]):
        return 1
    return 0