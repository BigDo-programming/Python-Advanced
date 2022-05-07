import sys
from io import StringIO
from pprint import pprint

input1 = """4
8 3 2 5
6 4 7 9
9 9 3 6
6 8 1 2
1,2 2,1 2,0"""

input2 = """3
7 8 4
3 1 5
6 4 9
0,2 1,0 2,2"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

import re
from collections import deque


def detonate(r, c, m):
    power = m[r][c]
    if m[r][c] > 0:
        m[r][c] = 0
    else:
        return matrix
    if 0 <= r - 1 < len(matrix) and 0 <= c - 1 < len(matrix):
        if m[r - 1][c - 1] > 0:
            m[r - 1][c - 1] -= power
    if 0 <= r - 1 < len(matrix) and 0 <= c < len(matrix):
        if m[r - 1][c] > 0:
            m[r - 1][c] -= power
    if 0 <= r - 1 < len(matrix) and 0 <= c + 1 < len(matrix):
        if m[r - 1][c + 1] > 0:
            m[r - 1][c + 1] -= power
    if 0 <= r < len(matrix) and 0 <= c - 1 < len(matrix):
        if m[r][c - 1] > 0:
            m[r][c - 1] -= power
    if 0 <= r < len(matrix) and 0 <= c + 1 < len(matrix):
        if m[r][c + 1] > 0:
            m[r][c + 1] -= power
    if 0 <= r + 1 < len(matrix) and 0 <= c - 1 < len(matrix):
        if m[r + 1][c - 1] > 0:
            m[r + 1][c - 1] -= power
    if 0 <= r + 1 < len(matrix) and 0 <= c < len(matrix):
        if m[r + 1][c] > 0:
            m[r + 1][c] -= power
    if 0 <= r + 1 < len(matrix) and 0 <= c + 1 < len(matrix):
        if m[r + 1][c + 1] > 0:
            m[r + 1][c + 1] -= power
    return matrix


matrix = []
alive_cell = []
size = int(input())
for row in range(size):
    value = [int(x) for x in input().split()]
    matrix.append(value)
data = input()

bombs = deque([int(x) for x in re.findall(r"\d", data)])

while bombs:
    row = bombs.popleft()
    col = bombs.popleft()

    matrix = detonate(row, col, matrix)

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] > 0:
            alive_cell.append(matrix[row][col])

print(f"Alive cells: {len(alive_cell)}")
print(f"Sum: {sum(alive_cell)}")
[print(*x) for x in matrix]

# ToDo 90/100
