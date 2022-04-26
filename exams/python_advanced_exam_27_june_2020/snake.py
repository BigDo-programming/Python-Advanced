import sys
from io import StringIO
from pprint import pprint

input1 = """6
-----S
----B-
------
------
--B---
--*---
left
down
down
down
left"""

input2 = """7
--***S-
--*----
--***--
---**--
---*---
---*---
---*---
left
left
left
down
down
right
right
down
left
down"""
# sys.stdin = StringIO(input1)

sys.stdin = StringIO(input2)

def next_step(row, col, side):
    if side == "up":
        return row - 1, col
    if side == "down":
        return row + 1, col
    if side == "left":
        return row, col - 1
    if side == "right":
        return row, col + 1


def is_outside(r, c, n):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True
    return False


snake_row = 0
snake_col = 0
lair = []
size = int(input())
matrix = []
for r in range(size):
    value = list(input())
    matrix.append(value)
    for c in range(size):
        if value[c] == 'S':
            snake_row, snake_col = r, c
            matrix[snake_row][snake_col] = "."
        if value[c] == 'B':
            lair.append((r, c))

food_quantity = 0

while True:
    command = input()


    snake_row, snake_col = next_step(snake_row, snake_col, command)

    if is_outside(snake_row, snake_col, size):
        break

    if matrix[snake_row][snake_col] == "*":
        food_quantity += 1

    if matrix[snake_row][snake_col] == "B":
        matrix[snake_row][snake_col] = "."
        lair.remove((snake_row, snake_col))
        snake_row, snake_col = lair.pop()

    if food_quantity == 10:
        matrix[snake_row][snake_col] = "S"
        break

    matrix[snake_row][snake_col] = "."

if food_quantity == 10:
    print("You won! You fed the snake.")
else:
    print("Game over!")
print(f"Food eaten: {food_quantity}")
[print(*x,sep='') for x in matrix]