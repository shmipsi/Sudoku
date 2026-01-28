import colored

# straight line to be printed for a sudoku grid
line_one = ["+","-","-","-","+","-","-","-","+","-","-","-","+"]
for i in range(13):
    line_one[i] = colored.stylize(line_one[i], colored.fg("red"))

def add_colors(list):
    for g in range(0, 13, 4):
        list[g] = colored.stylize(list[g], colored.fg("red"))


def print_array(array):
    line_number = 0
    for i in range(9):
        line_list = ["|"]
        for j in range(9):
            # adding "|" so everything is pretty
            line_list.append(array[i][j])
            if j==2 or j==5 or j==8: line_list.append("|")
        add_colors(line_list)
        # printing an array and adding straight line so everything is pretty
        if line_number==0: print(*line_one)
        print(*line_list)
        if line_number==2 or line_number==5 or line_number==8: print(*line_one)
        line_number += 1