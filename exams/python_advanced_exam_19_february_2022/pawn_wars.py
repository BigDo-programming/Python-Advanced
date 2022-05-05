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
- w - - - - - -
b - - - - - - -"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)


def matrix_():
    new_matrix_ = []
    my_row = []
    for r in range(8):
        for c in range(8):
            symbol = f"{chr(97 + c)}{8 - r}"
            my_row.append(symbol)

        new_matrix_.append(my_row.copy())
        my_row.clear()
    return new_matrix_


size = 8
matrix = []
black_row = 0
black_col = 0
white_row = 0
white_col = 0

for row in range(size):
    value = input().split()
    matrix.append(value)
    for col in range(size):
        if matrix[row][col] == "b":
            black_row, black_col = row, col
        if matrix[row][col] == "w":
            white_row, white_col = row, col

new_matrix = matrix_()

if abs(white_col - black_col) == 1:

    while True:

        if 0 <= white_row < len(matrix) and 0 <= white_col < len(matrix[0]):
            if matrix[white_row - 1][white_col - 1] == "b":
                print(f"Game over! White win, capture on {new_matrix[white_row - 1][white_col - 1]}.")
                exit()
            if matrix[white_row - 1][white_col + 1] == "b":
                print(f"Game over! White win, capture on {new_matrix[white_row - 1][white_col + 1]}.")
                exit()
            white_row, white_col = white_row - 1, white_col
            matrix[white_row][white_col] = "w"

        if 0 <= black_row < len(matrix) and 0 <= black_col < len(matrix[0]):
            if matrix[black_row + 1][black_col + 1] == "w":
                print(f"Game over! Black win, capture on {new_matrix[black_row + 1][black_col + 1]}.")
                exit()
            if matrix[black_row + 1][black_col - 1] == "w":
                print(f"Game over! Black win, capture on {new_matrix[black_row + 1][black_col - 1]}.")
                exit()
            black_row, black_col = black_row + 1, black_col
            matrix[black_row][black_col] = "b"

white = white_row - 0
black = abs(black_row - 8)

if black > white:
    print(f"Game over! White pawn is promoted to a queen at {new_matrix[0][white_col]}.")
else:
    print(f"Game over! Black pawn is promoted to a queen at {new_matrix[-1][black_col]}.")
# Todo 80/100 има грешка в този тест!!!
# print(black_row, black_col)
# print(white_row, white_col)
# pprint(new_matrix)


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
#
#         if 0 <= white_row - 1 < len(matrix) and 0 <= white_col - 1 < len(matrix[0]) and 0 <= white_row - 1 < len(
#                 matrix) and 0 <= white_col + 1 < len(matrix[0]):
#             if matrix[white_row - 1][white_col - 1] == "b":
#                 print(f"Game over! White win, capture on {new_matrix[white_row - 1][white_col - 1]}.")
#                 exit()
#             if matrix[white_row - 1][white_col + 1] == "b":
#                 print(f"Game over! White win, capture on {new_matrix[white_row - 1][white_col + 1]}.")
#                 exit()
#             white_row, white_col = white_row - 1, white_col
#             matrix[white_row][white_col] = "w"
#
#         if 0 <= black_row + 1 < len(matrix) and 0 <= black_col + 1 < len(matrix[0]) and 0 <= black_row + 1 < len(
#                 matrix) and 0 <= black_col - 1 < len(matrix[0]):
#             if matrix[black_row + 1][black_col + 1] == "w":
#                 print(f"Game over! Black win, capture on {new_matrix[black_row + 1][black_col + 1]}.")
#                 exit()
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
