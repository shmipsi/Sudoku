import colored

b2 = [
    [3, 9, 1, 2, 8, 6, 5, 7, 4],
    [4, 8, 7, 3, 5, 9, 1, 2, 6],
    [6, 5, 2, 7, 1, 4, 8, 3, 9],
    [8, 7, 5, 4, 3, 1, 6, 9, 2],
    [2, 1, 3, 9, 6, 7, 4, 8, 5],
    [9, 6, 4, 5, 2, 8, 7, 1, 3],
    [1, 4, 9, 6, 7, 3, 2, 5, 8],
    [5, 3, 8, 1, 4, 2, 9, 6, 7],
    [7, 2, 6, 8, 9, 5, 3, 4, 1]
    ]

# straight line to be printed
line_one = ["+","-","-","-","+","-","-","-","+","-","-","-","+"]
for i in range(13):
    line_one[i] = colored.stylize(line_one[i], colored.fg("red"))

# adding colors for lines with numbers
def add_colors(list):
    for g in range(0, 13, 4):
        list[g] = colored.stylize(list[g], colored.fg("red"))

# printing an array
def print_array(array):
    line_number = 0
    for i in range(9):
        line_list = ["|"]
        for j in range(9):
            # adding "|" so everything is prety
            line_list.append(array[i][j])
            if j==2 or j==5 or j==8: line_list.append("|")
        add_colors(line_list)
        # printing an array and adding straight line so everything is prety
        if line_number==0: print(*line_one)
        print(*line_list)
        if line_number==2 or line_number==5 or line_number==8: print(*line_one)
        line_number += 1

# check if sudoku solved right
# 1-right 0-wrong
def sudoku_check(array):
    # check horizontal sum
    for i in range(9):
        sum_hor = 0
        for j in range(9):
            sum_hor += array[i][j]
        if sum_hor != 45: return 0
    # check vertical sum
    for i in range(9):
        sum_vert = 0
        for j in range(9):
            sum_vert += array[j][i]
        if sum_vert != 45: return 0
    # check cell sum
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sum_cell = 0
            for k in range(3):
                for l in range(3):
                    sum_cell += array[i + k][j + l]
            if sum_cell != 45: return 0
    return 1

print_array(b2)
if sudoku_check(b2): print("That's correct!")
else: print("Nah that's bullshit")
