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

def move(_row, _col, direction):
    if direction == 'up':
        return _row - 1, _col
    if direction == 'down':
        return _row + 1, _col
    if direction == 'left':
        return _row, _col - 1
    if direction == 'right':
        return _row, _col + 1


def in_lair(snake_row, snake_col, lair):
    for i in lair:
        lair_row = i[0]
        lair_col = i[1]
        if not snake_row == lair_row and not snake_col == lair_col:
            return lair_row, lair_col


matrix = []
lair = []
food = 0
# win = True if food >= 10 else False
game_over = False
size = int(input())
snake_row, snake_col = 0, 0

for row in range(size):
    value = list(input())
    matrix.append(value)
    for col in range(size):
        if matrix[row][col] == 'S':
            snake_row, snake_col = row, col
        if matrix[row][col] == 'B':
            lair.append((row, col))
matrix[snake_row][snake_col] = '.'

while True:
    if food >= 10:
        break
    command = input()

    snake_row, snake_col = move(snake_row, snake_col, command)

    if snake_row < 0 or snake_row >= size or snake_col < 0 or snake_col >= size:
        game_over = True
        break
    if matrix[snake_row][snake_col] == 'B':
        matrix[snake_row][snake_col] = '.'
        snake_row, snake_col = in_lair(snake_row, snake_col, lair)
    if matrix[snake_row][snake_col] == '*':

        food += 1
    matrix[snake_row][snake_col] = '.'

if not food >= 10:
    print("Game over!")
else:
    print("You won! You fed the snake.")
    matrix[snake_row][snake_col] = 'S'
print(f"Food eaten: {food}")

[print(*x, sep='') for x in matrix]





# def next_step(row, col, side):
#     if side == "up":
#         return row - 1, col
#     if side == "down":
#         return row + 1, col
#     if side == "left":
#         return row, col - 1
#     if side == "right":
#         return row, col + 1
#
#
# def is_outside(r, c, n):
#     if r < 0 or r >= n or c < 0 or c >= n:
#         return True
#     return False
#
#
# snake_row = 0
# snake_col = 0
# lair = []
# size = int(input())
# matrix = []
# for r in range(size):
#     value = list(input())
#     matrix.append(value)
#     for c in range(size):
#         if value[c] == 'S':
#             snake_row, snake_col = r, c
#             matrix[snake_row][snake_col] = "."
#         if value[c] == 'B':
#             lair.append((r, c))
#
# food_quantity = 0
#
# while True:
#     command = input()
#
#
#     snake_row, snake_col = next_step(snake_row, snake_col, command)
#
#     if is_outside(snake_row, snake_col, size):
#         break
#
#     if matrix[snake_row][snake_col] == "*":
#         food_quantity += 1
#
#     if matrix[snake_row][snake_col] == "B":
#         matrix[snake_row][snake_col] = "."
#         lair.remove((snake_row, snake_col))
#         snake_row, snake_col = lair.pop()
#
#     if food_quantity == 10:
#         matrix[snake_row][snake_col] = "S"
#         break
#
#     matrix[snake_row][snake_col] = "."
#
# if food_quantity == 10:
#     print("You won! You fed the snake.")
# else:
#     print("Game over!")
# print(f"Food eaten: {food_quantity}")
# [print(*x,sep='') for x in matrix]