import re
import sys
from io import StringIO
from pprint import pprint

input1 = """4
4
(0, 3)
(1, 1)
(2, 2)
(3, 0)"""

input2 = """5
3
(1, 1)
(2, 4)
(4, 1)"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

import re


def in_matrix(row, col, matrix):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


def create_value(row, col, matrix):
    count = 0
    if in_matrix(row - 1, col - 1, matrix) and matrix[row - 1][col - 1] == "*":
        count += 1
    if in_matrix(row - 1, col, matrix) and matrix[row - 1][col] == "*":
        count += 1
    if in_matrix(row - 1, col + 1, matrix) and matrix[row - 1][col + 1] == "*":
        count += 1

    if in_matrix(row, col - 1, matrix) and matrix[row][col - 1] == "*":
        count += 1
    if in_matrix(row, col + 1, matrix) and matrix[row][col + 1] == "*":
        count += 1

    if in_matrix(row + 1, col - 1, matrix) and matrix[row + 1][col - 1] == "*":
        count += 1
    if in_matrix(row + 1, col, matrix) and matrix[row + 1][col] == "*":
        count += 1
    if in_matrix(row + 1, col + 1, matrix) and matrix[row + 1][col + 1] == "*":
        count += 1
    return count


matrix = []
size = int(input())
for r in range(size):
    value = [None] * size
    matrix.append(value)

n = int(input())
for _ in range(n):
    data = input()
    bomb_row, bomb_col = [int(x) for x in re.findall(r"\d+", data)]
    matrix[bomb_row][bomb_col] = "*"

for row in range(size):
    for col in range(size):
        if not matrix[row][col] == "*":
            count = create_value(row, col, matrix)
            matrix[row][col] = count

[print(*x) for x in matrix]