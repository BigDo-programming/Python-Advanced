import sys
from io import StringIO
from pprint import pprint

input1 = """5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0"""

input2 = """8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22"""
input3 = """"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


def next_step(b_row, b_col, move_to):
    if move_to == "up":
        return b_row - 1, b_col

    if move_to == "down":
        return b_row + 1, b_col

    if move_to == "left":
        return b_row, b_col - 1

    if move_to == "right":
        return b_row, b_col + 1,


matrix = []
start_row = 0
start_col = 0
bunny_path = ""
paths = ["up", "down", "left", 'right']
n = int(input())
for i in range(n):
    value = [x for x in input().split()]
    matrix.append(value)
    for j in range(n):
        if matrix[i][j] == "B":
            start_row, start_col = i, j

for direction in paths:
    eggs = 0
    bunny_row, bunny_col = start_row, start_col
    while True:
        bunny_row, bunny_col = next_step(bunny_row, bunny_col, direction)
        if bunny_row < 0 or bunny_row >= len(matrix) or bunny_col < 0 or bunny_col >= len(matrix):
            break
        if matrix[bunny_row][bunny_col] == "X":
            break
        eggs += int(matrix[bunny_row][bunny_col])
    print(eggs)

# pprint(matrix)










# def move_up(row, col):
#     return row - 1, col


# def move_down(row, col):
#     return row + 1, col
#
#
# def move_left(row, col):
#     return row, col - 1
#
#
# def move_right(row, col):
#     return row, col + 1
#
#
# bunny_row, bunny_col = 0, 0
#
# matrix = []
# n = int(input())
# for row in range(n):
#     value = [x for x in input().split()]
#     matrix.append(value)
#
#     for col in range(n):
#         if value[col] == "B":
#             bunny_row = row
#             bunny_col = col
#
# directions = {
#     "up": move_up,
#     "down": move_down,
#     "left": move_left,
#     "right": move_right,
# }
#
# best_score = float("-inf")
# best_dir = ""
# best_path = []
# for direction, step in directions.items():
#     current_row, current_col = bunny_row, bunny_col
#
#     current_score = 0
#     path = []
#     while True:
#         current_row, current_col = step(current_row, current_col)
#         if current_row < 0 or current_col < 0 or current_row >= n or current_col >= n:
#             break
#         if matrix[current_row][current_col] == "X":
#             break
#
#         path.append([current_row,current_col])
#         current_score += int(matrix[current_row][current_col])
#     if current_score > best_score and path:
#         best_score = current_score
#         best_dir = direction
#         best_path = path
#
# print(best_dir)
#
# [print(x) for x in best_path]
# print(best_score)
