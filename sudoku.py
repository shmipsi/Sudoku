import colored

# 2
b2 = [
    [3, 9, 1, "-", 8, 6, 5, 7, 4],
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

# dup checks
def dup_check_line(array,i,j):
    dup = array[i][j]
    for k in range(9):
        if j!=k and dup==array[i][k]: return 0
    return 1

# check if sudoku solved right
# 1-right 0-wrong
def sudoku_check_correctness(array):
    # check horizontal sum and duplicates
    for i in range(9):
        sum_hor = 0
        for j in range(9):
            sum_hor += array[i][j]
            dup_check_line(array,i,j)
        if sum_hor!=45: return 0
    # check vertical sum and duplicates
    for j in range(9):
        sum_vert = 0
        for i in range(9):
            sum_vert += array[i][j]
            dup_check_line(array,i,j)
        if sum_vert != 45: return 0
    # check cell sum and duplicates
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sum_cell = 0
            for k in range(3):
                for l in range(3):
                    sum_cell += array[i + k][j + l]
                    dup = array[i+k][j+l]
                    for n in range(3):
                        for m in range(3):
                            if k!=n and l!=m and dup==array[i+n][j+m]: return 0
            if sum_cell != 45: return 0
    return 1

# solve the sudoku
def sudoku_solve(array):
    empty_cells=[[],[]]
    for i in range(9):
        for j in range(9):
            if array[i][j]=="-":
                empty_cells[0].append(i)
                empty_cells[1].append(i)
    range_l = len(empty_cells[0])
    digit = 1
    # there must be something else so everything tryes itself again if not correct
    for k in range(range_l):
        i = empty_cells[0][k]
        j = empty_cells[1][k]
        array[i][j] = digit
        print(digit)
        if dup_check_line(array,i,j) == 0: digit += 1
        # add here vert and cell check
        print_array(array)
        if digit > 9:
            digit = 0
            continue
        if i==9 and j==9 and digit>9: return "Nah that's bullshit"
    return array

def switch(value):
    if value==1:
        print_array(b2)
    elif value==2:
        print_array(b2)
    elif value==3:
        print_array(b2)
        b2 = sudoku_solve(b2)
    elif value==4:
        print_array(b2)
        if sudoku_check_correctness(b2): print("That's correct!")
        else: print("Nah that's bullshit")
    else: print("error")


# main code
print("-------------------------Welcome to Sudoku!-------------------------")
print("Now you can choose what you want to do:")
print("1 - check if sudoku is valid")
print("2 - give you a sudoku to solve")
print("3 - solve the sudoku")
print("4 - tell you if sudoku solved correctly")
switch(int(input()))