import sys

from io import StringIO
from pprint import pprint

input1 = """5
up right right up right
* * * c *
* * * e *
* * c * *
s * * c *
* * c * *"""
input2 = """4
up right right right down
* * * e
* * c *
* s * c
* * * *"""
input3 = """6
left left down right up left left down down down
* * * * * *
e * * * c *
* * c s * *
* * * * * *
c * * * c *
* * c * * *"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)
from collections import deque


def move(row, col, command, n):
    if command == "left":
        new_row, new_col = row, col - 1
        if 0 <= row < n and 0 <= col - 1 < n:
            return new_row, new_col
        return row, col

    if command == "right":
        new_row, new_col = row, col + 1
        if 0 <= row < n and 0 <= col + 1 < n:
            return new_row, new_col
        return row, col

    if command == "up":
        new_row, new_col = row - 1, col
        if 0 <= row - 1 < n and 0 <= col < n:
            return new_row, new_col
        return row, col

    if command == "down":

        new_row, new_col = row + 1, col
        if 0 <= row + 1 < n and 0 <= col < n:
            return new_row, new_col
        return row, col


n = int(input())
miner_row = 0
miner_col = 0
coal = 0
direction = deque(input().split())
matrix = []
for i in range(n):
    value = [x for x in input().split()]
    matrix.append(value)
    for j in range(n):
        if matrix[i][j] == "s":
            miner_row, miner_col = i, j
        if matrix[i][j] == "c":
            coal += 1
is_gameover = False
while direction:
    if coal == 0:
        break

    command = direction.popleft()
    miner_row, miner_col = move(miner_row, miner_col, command, n)
    if matrix[miner_row][miner_col] == "e":
        print(f"Game over! ({miner_row}, {miner_col})")
        is_gameover = True
        break
    if matrix[miner_row][miner_col] == "c":
        coal -= 1
        if coal == 0:
            print(f"You collected all coal! ({miner_row}, {miner_col})")
            break
    matrix[miner_row][miner_col] = "*"


if not direction and not is_gameover and coal > 0:
    print(f"{coal} pieces of coal left. ({miner_row}, {miner_col})")


#
# def move(move_row, move_col, move_command, move_size):
#     if move_command == 'up':
#         if 0 <= move_row - 1 < move_size and 0 <= move_col < move_size:
#             return move_row - 1, move_col
#
#     if move_command == 'down':
#         if 0 <= move_row + 1 < move_size and 0 <= move_col < move_size:
#             return move_row + 1, move_col
#     if move_command == 'left':
#         if 0 <= move_row < move_size and 0 <= move_col - 1 < move_size:
#             return move_row, move_col - 1
#     if move_command == 'right':
#         if 0 <= move_row < move_size and 0 <= move_col + 1 < move_size:
#             return move_row, move_col + 1
#     return move_row, move_col
#
# size = int(input())
# all_coal = 0
# matrix = []
# miner_row, miner_col = 0, 0
# is_end = False
# command = input().split()
# for row in range(size):
#     value = input().split()
#     matrix.append(value)
#     for col in range(size):
#
#         if matrix[row][col] == 's':
#             miner_row, miner_col = row, col
#         elif matrix[row][col] == 'c':
#             all_coal += 1
# for i in command:
#     miner_row, miner_col = move(miner_row, miner_col, i, size)
#     if matrix[miner_row][miner_col] == 'c':
#         matrix[miner_row][miner_col] = '*'
#         all_coal -= 1
#         if all_coal == 0:
#             print(f"You collected all coal! ({miner_row}, {miner_col})")
#             break
#
#     elif matrix[miner_row][miner_col] == 'e':
#         print(f"Game over! ({miner_row}, {miner_col})")
#         is_end = True
#         break
# if not is_end and all_coal > 0:
#     print(f"{all_coal} pieces of coal left. ({miner_row}, {miner_col})")
