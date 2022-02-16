from sys import stdin
from sys import stdout


arr = [list(map(int, stdin.readline().split())) for _ in range(9)]

zero = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]


def is_not_exist_in_row(num, row_num):
    for i in range(9):
        if num == arr[row_num][i]:
            return False
    return True


def is_not_exist_in_column(num, column_num):
    for i in range(9):
        if num == arr[i][column_num]:
            return False
    return True


def is_not_exist_in_box(num, row_num, column_num):
    x = row_num // 3 * 3
    y = column_num // 3 * 3
    for i in range(3):
        for j in range(3):
            if num == arr[x+i][y+j]:
                return False
    return True


def sudoku(num):
    if num == len(zero):
        for i in range(9):
            stdout.write(' '.join(map(str, arr[i]))+'\n')
        exit(0)

    for i in range(1, 10):
        x, y = zero[num]
        if is_not_exist_in_row(i, x) and is_not_exist_in_column(i, y) and is_not_exist_in_box(i, x, y):
            arr[x][y] = i
            sudoku(num+1)
            arr[x][y] = 0


sudoku(0)
