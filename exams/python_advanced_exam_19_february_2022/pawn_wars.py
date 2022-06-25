import sys
from io import StringIO
from pprint import pprint

input1 = """- - - - - - b -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -"""

input2 = """- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
b - - - - - - -
- w - - - - - -
- - - - - - - -"""

input3 = """- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
b - - - - - - -
- w - - - - - -"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from math import ceil

size = 8
matrix = []
white_row, white_col = 0, 0
black_row, black_col = 0, 0

matrix_bord = []
for bord_row in range(size, 0, -1):
    value = [f'{chr(97 + x)}{bord_row}' for x in range(size)]
    matrix_bord.append(value)

for row in range(size):
    value = input().split()
    matrix.append(value)
    for col in range(size):
        if matrix[row][col] == 'b':
            black_row, black_col = row, col

        elif matrix[row][col] == 'w':
            white_row, white_col = row, col

if not abs(black_col - white_col) == 1:
    if (size - black_row) > white_row:
        print(f"Game over! White pawn is promoted to a queen at {matrix_bord[size - size][white_col]}.")

    else:
        print(f"Game over! Black pawn is promoted to a queen at {matrix_bord[size - 1][black_col]}.")


else:
    if abs(black_row - white_row) % 2 == 0:
        print(f"Game over! Black win, capture on {matrix_bord[black_row + ceil(abs(black_row - white_row)/2)][white_col]}.")

    else:
        print(f"Game over! White win, capture on {matrix_bord[white_row-ceil(abs(black_row - white_row)/2)][black_col]}.")


#
# def in_matrix(matrix_row, matrix_col, matrix):
#     if 0 <= matrix_row < len(matrix) and 0 <= matrix_col < len(matrix[0]):
#         return True
#     return False
#
#
# def matrix_():
#     new_matrix_ = []
#     my_row = []
#     for r in range(8):
#         for c in range(8):
#             symbol = f"{chr(97 + c)}{8 - r}"
#             my_row.append(symbol)
#
#         new_matrix_.append(my_row.copy())
#         my_row.clear()
#     return new_matrix_
#
#
# size = 8
# matrix = []
# black_row = 0
# black_col = 0
# white_row = 0
# white_col = 0
#
# for row in range(size):
#     value = input().split()
#     matrix.append(value)
#     for col in range(size):
#         if matrix[row][col] == "b":
#             black_row, black_col = row, col
#         if matrix[row][col] == "w":
#             white_row, white_col = row, col
#
# new_matrix = matrix_()
#
# if abs(white_col - black_col) == 1:
#
#     while True:
#         if in_matrix(white_row - 1, white_col - 1, matrix):
#             if matrix[white_row - 1][white_col - 1] == "b":
#                 print(f"Game over! White win, capture on {new_matrix[white_row - 1][white_col - 1]}.")
#                 exit()
#         if in_matrix(white_row - 1, white_col + 1, matrix):
#             if matrix[white_row - 1][white_col + 1] == "b":
#                 print(f"Game over! White win, capture on {new_matrix[white_row - 1][white_col + 1]}.")
#                 exit()
#             white_row, white_col = white_row - 1, white_col
#             matrix[white_row][white_col] = "w"
#         if in_matrix(black_row+1,black_col+1,matrix):
#
#             if matrix[black_row + 1][black_col + 1] == "w":
#                 print(f"Game over! Black win, capture on {new_matrix[black_row + 1][black_col + 1]}.")
#                 exit()
#         if in_matrix(black_row + 1, black_col - 1, matrix):
#             if matrix[black_row + 1][black_col - 1] == "w":
#                 print(f"Game over! Black win, capture on {new_matrix[black_row + 1][black_col - 1]}.")
#                 exit()
#             black_row, black_col = black_row + 1, black_col
#             matrix[black_row][black_col] = "b"
#
# white = white_row - 0
# black = abs(black_row - 8)
#
# if black > white:
#     print(f"Game over! White pawn is promoted to a queen at {new_matrix[0][white_col]}.")
# else:
#     print(f"Game over! Black pawn is promoted to a queen at {new_matrix[-1][black_col]}.")
# # Todo 90/100
