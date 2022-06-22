import sys
from io import StringIO
from pprint import pprint

input1 = """Hello
4
P---
Mark
-l-y
--e-
4
down
right
right
right"""

input2 = """Initial
5
-----
t-r--
--Pa-
--S--
z--t-
4
up
left
left
left"""

input3 = """I
5
-----
t-r--
--Pa-
--S--
z--t-
4
left
left
left
left"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)


def move(row_, col_, direction):
    if direction == 'up':
        return row_ - 1, col_

    if direction == 'down':
        return row_ + 1, col_

    if direction == 'left':
        return row_, col_ - 1

    if direction == 'right':
        return row_, col_ + 1


matrix = []
string = input()
size = int(input())
p_row, p_col = 0, 0

for r in range(size):
    matrix.append(list(input()))
    for c in range(size):
        if matrix[r][c] == "P":
            p_row, p_col = r, c

matrix[p_row][p_col] = '-'

n = int(input())
for i in range(n):
    command = input()
    row, col = move(p_row, p_col, command)
    if row < 0 or row >= size or col < 0 or col >= size:
        if string:
            string = string[:-1]
    else:
        p_row, p_col = row, col
        if not matrix[p_row][p_col] == '-':
            string += matrix[p_row][p_col]
            matrix[p_row][p_col] = '-'

matrix[p_row][p_col] = 'P'
print(string)
[print(*x, sep='') for x in matrix]

