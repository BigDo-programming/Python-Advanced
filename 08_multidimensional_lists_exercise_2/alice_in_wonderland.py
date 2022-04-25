import sys
from io import StringIO

input1 = """5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left"""

input2 = """7
. A . 1 1 . .
9 . . . 6 . 5
. 6 . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2
left
down
down
right"""
# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)


def alice_next_step(row, col, side):
    if side == "up":
        return row - 1, col
    if side == "down":
        return row + 1, col
    if side == "left":
        return row, col - 1
    if side == "right":
        return row, col + 1


def is_outside(r, c, n):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True
    return False


a_row = 0
a_col = 0
n = int(input())
matrix = []
for r in range(n):
    value = list(input().split())
    matrix.append(value)
    for c in range(n):
        if value[c] == "A":
            a_row, a_col = r, c
matrix[a_row][a_col] = "*"
teabag = 0

while True:
    command = input()

    a_row, a_col = alice_next_step(a_row, a_col, command)
    if is_outside(a_row, a_col, n):
        break
    cell_value = matrix[a_row][a_col]
    matrix[a_row][a_col] = "*"

    if cell_value == "R":
        break

    if cell_value.isdigit():
        teabag += int(cell_value)

        if teabag >= 10:
            break

if teabag >= 10:

    print(f"She did it! She went to the party.")
    [print(*x) for x in matrix]
else:

    print(f"Alice didn't make it to the tea party.")
    [print(*x) for x in matrix]
