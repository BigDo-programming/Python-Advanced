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


from collections import deque


def move(row, col, diraction):
    if diraction == 'up':
        return row - 1, col
    if diraction == 'down':
        return row + 1, col
    if diraction == 'left':
        return row, col - 1
    if diraction == 'right':
        return row, col + 1


n = 6
rover_row, rover_col = 0, 0
water, metal, concrete = 0, 0, 0
matrix = []
for row in range(n):
    value = input().split()
    matrix.append(value)
    for col in range(n):
        if matrix[row][col] == "E":
            rover_row, rover_col = row, col

commands = deque(input().split(", "))
while commands:
    command = commands.popleft()
    rover_row, rover_col = move(rover_row, rover_col, command)
    rover_row = rover_row % n
    rover_col = rover_col % n
    # print(rover_row,rover_col)
    if matrix[rover_row][rover_col] == "-":
        continue
    if matrix[rover_row][rover_col] == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break
    if matrix[rover_row][rover_col] == "W":
        water += 1
        print(f"Water deposit found at ({rover_row}, {rover_col})")

    elif matrix[rover_row][rover_col] == "M":
        metal += 1
        print(f"Metal deposit found at ({rover_row}, {rover_col})")

    elif matrix[rover_row][rover_col] == "C":
        concrete += 1
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")

# [print(x) for x in matrix]
if water > 0 and concrete > 0 and metal > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")



# def move(move_row, move_col, move_size, direction):
#     if direction == "up":
#         return next_step(move_row - 1, move_col, move_size)
#     if direction == "down":
#         return next_step(move_row + 1, move_col, move_size)
#     if direction == "left":
#         return next_step(move_row, move_col - 1, move_size)
#     if direction == "right":
#         return next_step(move_row, move_col + 1, move_size)
#
#
# def next_step(next_row, next_col, size):
#     if 0 > next_row or next_row >= size:
#         next_row = next_row % size
#     if 0 > next_col or next_col >= size:
#         next_col = next_col % size
#     return next_row, next_col
#
#
# matrix = []
# size = 6
# rover_row = 0
# rover_col = 0
# water = 0
# metal = 0
# concrete = 0
# for row in range(size):
#     value = input().split()
#     matrix.append(value)
#     for col in range(size):
#         if matrix[row][col] == "E":
#             rover_row, rover_col = row, col
#
# command = input().split(", ")
# for i in command:
#     rover_row, rover_col = move(rover_row, rover_col, size, i)
#     if matrix[rover_row][rover_col] == "W":
#         water += 1
#         print(f"Water deposit found at ({rover_row}, {rover_col})")
#     elif matrix[rover_row][rover_col] == "M":
#         metal += 1
#         print(f"Metal deposit found at ({rover_row}, {rover_col})")
#     elif matrix[rover_row][rover_col] == "C":
#         concrete += 1
#         print(f"Concrete deposit found at ({rover_row}, {rover_col})")
#     elif matrix[rover_row][rover_col] == "R":
#         print(f"Rover got broken at ({rover_row}, {rover_col})")
#         break
#
# if water > 0 and metal > 0 and concrete > 0:
#     print("Area suitable to start the colony.")
# else:
#     print("Area not suitable to start the colony.")
#
