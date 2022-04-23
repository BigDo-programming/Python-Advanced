import sys
from io import StringIO
from pprint import pprint

input1 = """3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END"""

input2 = """4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)


def is_valid_coordinate(r, c, n):
    return 0 <= r < n and 0 <= c < n


matrix = []
n = int(input())
for i in range(n):
    value = [int(x) for x in input().split()]
    matrix.append(value)
command = input()
while not command == "END":
    command_split = command.split()
    action = command_split[0]
    row, col, value = [int(x) for x in command_split[1:]]

    if action == "Add":
        if is_valid_coordinate(row, col, n):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")

    if action == "Subtract":
        if is_valid_coordinate(row, col, n):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

    command = input()

for i in matrix:
    print(*i)