import sys
from io import StringIO

input1 = """"""

input2 = """"""

input3 = """"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


def move(row, col, destination):
    if destination == 'up':
        return row - 1, col

    if destination == 'down':
        return row + 1, col

    if destination == 'left':
        return row, col - 1

    if destination == 'right':
        return row, col + 1


matrix = []

m_row, m_col = 0, 0
size = int(input())
for r in range(size):

    # value = input().split()
    value = [int(x) for x in input().split()]
    matrix.append(value)

    for c in range(size):
        if matrix[r][c] == '':
            m_row, m_col = r, c
