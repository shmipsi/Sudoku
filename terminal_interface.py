import colored

# straight line to be printed for a sudoku grid
line_one = ["+","-","-","-","+","-","-","-","+","-","-","-","+"]
for element in range(13):
    line_one[element] = colored.stylize(line_one[element], colored.fg("red"))

def add_colors(list):
    for element in range(0, 13, 4):
        list[element] = colored.stylize(list[element], colored.fg("red"))


def print_array(sudoku):
    line_number = 0
    for row in sudoku:
        line_list = ["|"]
        for value in range(9):
            if row[value] == 0:
                line_list.append(" ") 
            else:
                line_list.append(row[value])
            # separator
            if value==2 or value==5 or value==8: line_list.append("|")
        add_colors(line_list)
        # printing an array and adding separators
        if line_number==0: print(*line_one)
        print(*line_list)
        if line_number==2 or line_number==5 or line_number==8: print(*line_one)
        line_number += 1