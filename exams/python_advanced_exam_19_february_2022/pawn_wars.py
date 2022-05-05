import sys
from io import StringIO

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

input3 = """"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

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
if abs(white_col - black_col) == 1:
    # captures()
    print("fight")
else:

    white = white_row - 0
    black = abs(black_row - 8)
    if black > white:
        print("white")
    else:
        print("black")
#     print(white)
#     print(black)
# #     # go_for_queen()
# print(white_row)
# print(black_row)
