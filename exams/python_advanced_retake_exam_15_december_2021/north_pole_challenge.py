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
down-3"""

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
def move(direction, row, col):
    if direction == "up":
        return row - 1, col

    if direction == "down":
        return row + 1, col
        pass

    if direction == "left":
        return row, col - 1
        pass
    if direction == "right":
        return row, col + 1


matrix = []
my_row = 0
my_col = 0
n, m = [int(x) for x in input().split(', ')]
for row in range(n):
    value = input().split()
    matrix.append(value)
    for col in range(m):
        if matrix[row][col] == "Y":
            my_row, my_col = row, col
pprint(matrix)
command = input()
while not command == "End":
    direction, steps = command.split("-")
    for i in range(int(steps)):
        my_row, my_col = move(direction, my_row, my_col)
        # prawim prowerka ako e izlqzal ot matricata da mine ot drugata strana i prawim prowerka kakwo ima w kletkata za da go wzemem i mestim sebesi i èrtaem pyt
        print(my_row, my_col)

    command = input()
