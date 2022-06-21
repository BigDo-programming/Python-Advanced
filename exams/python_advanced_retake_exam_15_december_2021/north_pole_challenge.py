import sys
from io import StringIO
from pprint import pprint

input1 = """6, 5
. . . . .
C . . G .
. C . . .
G . . C .
. D . . D
Y . . . G
left-3
up-1
left-2
right-7
up-1
End"""

input2 = """5, 6
. . . . . .
. . . . . .
Y C D D . .
. . . C . .
. . . C . .
right-3
down-3
End"""

input3 = """5, 2
. .
. .
. Y
. .
. G
up-1
left-11
down-10
End"""

sys.stdin = StringIO(input1)


# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

matrix = []
christmas_decorations = 0
gifts = 0
cookies = 0
item = 0
santa_row, santa_col = 0, 0
n, m = [int(x) for x in input().split(", ")]
for row in range(n):
    value = input().split()
    matrix.append(value)
    for col in range(m):
        if matrix[row][col] == 'Y':
            santa_row, santa_col = row, col
        if matrix[row][col] in 'D, G, C':
            item += 1

matrix[santa_row][santa_col] = 'x'


def move(row, col, move_to):
    if move_to == 'up':
        return row - 1, col
    if move_to == 'down':
        return row + 1, col
    if move_to == 'left':
        return row, col - 1
    if move_to == 'right':
        return row, col + 1


collect_all = False
while True:
    if collect_all:
        break
    command = input()
    if command == 'End':
        break

    direction = command.split('-')[0]
    step = int(command.split('-')[1])
    for i in range(step):
        santa_row, santa_col = move(santa_row, santa_col, direction)
        santa_row = santa_row % n
        santa_col = santa_col % m
        if matrix[santa_row][santa_col] == 'D':
            item -= 1
            christmas_decorations += 1
        if matrix[santa_row][santa_col] == 'G':
            item -= 1
            gifts += 1
        if matrix[santa_row][santa_col] == 'C':
            item -= 1
            cookies += 1
        matrix[santa_row][santa_col] = 'x'
        if item == 0:
            collect_all = True
            break

matrix[santa_row][santa_col] = 'Y'

if collect_all:
    print("Merry Christmas!")
print("You've collected:")
print(f'- {christmas_decorations} Christmas decorations')
print(f'- {gifts} Gifts')
print(f'- {cookies} Cookies')
[print(*x) for x in matrix]
