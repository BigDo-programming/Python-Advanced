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

sys.stdin = StringIO(input2)


# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)








































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