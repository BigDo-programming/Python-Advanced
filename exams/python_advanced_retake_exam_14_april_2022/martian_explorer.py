import sys
from io import StringIO
from pprint import pprint

input1 = """- R - - - -
- - - - - R
- E - R - -
- W - - - -
- - - C - -
M - - - - -
down, right, down, right, down, left, left, left"""

input2 = """R - - - - -
- - C - - -
- - - - M -
- - W - - -
- E - W - R
- - - - - -
up, right, down, right, right, right"""

input3 = """R - - - - -
- - C - - -
- - - - M -
C - M - R M
- E - W - -
- - - - - -
right, right, up, left, left, left, left, left"""

# sys.stdin = StringIO(input1)


# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)


def move(move_row, move_col, move_size, direction):
    if direction == "up":
        return next_step(move_row - 1, move_col, move_size)
    if direction == "down":
        return next_step(move_row + 1, move_col, move_size)
    if direction == "left":
        return next_step(move_row, move_col - 1, move_size)
    if direction == "right":
        return next_step(move_row, move_col + 1, move_size)


def next_step(next_row, next_col, size):
    if 0 > next_row or next_row >= size:
        next_row = next_row % size
    if 0 > next_col or next_col >= size:
        next_col = next_col % size
    return next_row, next_col


matrix = []
size = 6
rover_row = 0
rover_col = 0
deposit = 0
for row in range(size):
    value = input().split()
    matrix.append(value)
    for col in range(size):
        if matrix[row][col] == "E":
            rover_row, rover_col = row, col
        if matrix[row][col] == "W" or matrix[row][col] == "M" or matrix[row][col] == "C":
            deposit += 1
command = input().split(", ")
for i in command:
    rover_row, rover_col = move(rover_row, rover_col, size, i)
    if matrix[rover_row][rover_col] == "W":
        deposit -= 1
        print(f"Water deposit found at ({rover_row}, {rover_col})")
    elif matrix[rover_row][rover_col] == "M":
        deposit -= 1
        print(f"Metal deposit found at ({rover_row}, {rover_col})")
    elif matrix[rover_row][rover_col] == "C":
        deposit -= 1
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")
    elif matrix[rover_row][rover_col] == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

if deposit == 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
# Todo 92/100
