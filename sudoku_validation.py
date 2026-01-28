
def validate_format(sudoku):
    if not isinstance(sudoku, list) or len(sudoku) != 9:
        return "sudoku format error"
    return "Ok"

def validate_negative(sudoku):
    for row in sudoku:
        for value in row:
            if value < 0:
                return "sudoku contains negative values"
    return "Ok"





def validate_sudoku(sudoku):
    format_valid = validate_format(sudoku)
    negative_valid = validate_negative(sudoku)

    print(f"Format validation: {format_valid}")
    print(f"Negative validation: {negative_valid}")