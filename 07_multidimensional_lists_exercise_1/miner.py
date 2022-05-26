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