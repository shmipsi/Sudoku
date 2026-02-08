import sudoku_validation

def find_empty_cell(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return (row, col)
    return None

def solve_sudoku(sudoku):
    if not sudoku_validation.validate_all(sudoku):
        return "Invalid sudoku", None
    
    while find_empty_cell(sudoku) is not None:
        row, col = find_empty_cell(sudoku)
        available_values = set(range(1, 10))

        for value in range(1, 10):
            # box
            box_row_start = (row // 3) * 3
            box_col_start = (col // 3) * 3
            for r in range(box_row_start, box_row_start + 3):
                for c in range(box_col_start, box_col_start + 3):
                    if sudoku[r][c] == value:
                        available_values.discard(value)
            # row
            if value in sudoku[row]:
                available_values.discard(value)
            # column
            if value in [sudoku[r][col] for r in range(9)]:
                available_values.discard(value)
            
        if not available_values:
            return "No valid value found for this cell", sudoku

        if len(available_values) == 1:
            sudoku[row][col] = available_values.pop()
        

    return "Sudoku solved successfully", sudoku
