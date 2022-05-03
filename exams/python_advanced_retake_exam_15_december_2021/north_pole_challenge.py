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
def found_next_step(r, c, m):
    if 0 > r or r >= len(m):
        r = r % len(m)
    if 0 > c or c >= len(m[0]):
        c = c % len(m[0])

    return r, c


def move(direction, row, col, matrix):
    if direction == "up":
        return found_next_step(row - 1, col, matrix)

    if direction == "down":
        return found_next_step(row + 1, col, matrix)

    if direction == "left":
        return found_next_step(row, col - 1, matrix)

    if direction == "right":
        return found_next_step(row, col + 1, matrix)


matrix = []
my_row = 0
my_col = 0
christmas_decorations = 0
gifts = 0
cookies = 0
items_for_collect = 0
n, m = [int(x) for x in input().split(', ')]
for row in range(n):
    value = input().split()
    matrix.append(value)
    for col in range(m):
        if matrix[row][col] == "Y":
            my_row, my_col = row, col
            matrix[my_row][my_col] = "x"
        if matrix[row][col] == "D" or matrix[row][col] == "C" or matrix[row][col] == "G":
            items_for_collect += 1

command = input()
while not command == "End":
    direction, steps = command.split("-")
    for i in range(int(steps)):
        my_row, my_col = move(direction, my_row, my_col, matrix)
        if matrix[my_row][my_col] == "D":
            christmas_decorations += 1

        if matrix[my_row][my_col] == "G":
            gifts += 1
        if matrix[my_row][my_col] == "C":
            cookies += 1
        matrix[my_row][my_col] = "x"

    command = input()

matrix[my_row][my_col] = "Y"
if items_for_collect == 0:
    print("Merry Christmas!")
print(f"You've collected:")
print(f"- {christmas_decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
[print(*x) for x in matrix]
#  Todo i thing in "North Pole Challenge" have error input. Missing "End"
