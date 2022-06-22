import sys
from io import StringIO

input1 = """"""

input2 = """"""

input3 = """"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


def move(row_, col_, destination):
    if destination == 'up':
        return row_ - 1, col_

    if destination == 'down':
        return row_ + 1, col_

    if destination == 'left':
        return row_, col_ - 1

    if destination == 'right':
        return row_, col_ + 1


matrix = []

m_row, m_col = 0, 0
size = int(input())
for row in range(size):

    # value = input().split()
    value = [int(x) for x in input().split()]
    matrix.append(value)

    for col in range(size):
        if matrix[row][col] == '':
            m_row, m_col = row, col
