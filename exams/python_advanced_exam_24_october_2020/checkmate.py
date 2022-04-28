import sys

from io import StringIO
from pprint import pprint

input1 = """. . . . . . . .
Q . . . . . . .
. K . . . Q . .
. . . Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. Q . Q . . . ."""

input2 = """. . . . . . . .
. . . Q . . . .
. . . . . . . .
. . . . . . . .
Q . . . Q . . .
. . K . . . . .
. . . . . . Q .
. . . Q . . . ."""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

matrix = []
king_row = 0
king_col = 0

for r in range(8):
    value = input().split()
    matrix.append(value)
    for c in range(8):

        if matrix[r][c] == "K":
            king_row, king_col = r, c


direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1),
}
my_direction = [
    "up",
    "down",
    "left",
    "right",
    "up_left",
    "up_right",
    "down_left",
    "down_right"]

attacked_quin = []

for i in my_direction:
    start_r, start_c = king_row, king_col
    while True:

        start_r += direction[i][0]
        start_c += direction[i][1]
        if start_r < 0 or start_c < 0 or start_r >= len(matrix) or start_c >= len(matrix):
            break

        if matrix[start_r][start_c] == "Q":
            attacked_quin.append([start_r, start_c])
            break
if attacked_quin:
    for i in attacked_quin:
        print(i)
else:
    print("The king is safe!")