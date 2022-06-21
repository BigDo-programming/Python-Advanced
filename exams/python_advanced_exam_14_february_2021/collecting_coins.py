import sys
from io import StringIO
from pprint import pprint

input1 = """5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
left
right
right
up
up
right"""

input2 = """8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
down
up
left"""

input3 = """"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


def move(row, col, direction):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


path = []
coins = 0
size = int(input())
matrix = []
player_row, player_col = 0, 0
for r in range(size):
    value = [int(x) if x.isdigit() else str(x) for x in input().split()]
    matrix.append(value)
    for c in range(size):
        if matrix[r][c] == 'P':
            player_row, player_col = r, c

matrix[player_row][player_col] = 0
path.append(f'[{player_row}, {player_col}]')


while coins < 100:
    command = input()

    player_row, player_col = move(player_row, player_col, command)
    player_row %= size
    player_col %= size

    path.append(f'[{player_row}, {player_col}]')
    if matrix[player_row][player_col] == 'X':
        coins *= 0.5

        break
    coins += matrix[player_row][player_col]
    matrix[player_row][player_col] = 0

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {int(coins)} coins.")
print('Your path:')
[print(x) for x in path]



# def move(direction, row, col):
#     if direction == "up":
#         return row - 1, col
#     if direction == "down":
#         return row + 1, col
#     if direction == "left":
#         return row, col - 1
#     if direction == "right":
#         return row, col + 1
#
#
# path = []
# coins = 0
# size = int(input())
# player_row = 0
# player_col = 0
#
# matrix = []
# for r in range(size):
#     value = input().split()
#     matrix.append(value)
#     for c in range(size):
#         if matrix[r][c] == "P":
#             player_row, player_col = r, c
# path.append([player_row, player_col])
# while True:
#     command = input()
#     player_row, player_col = move(command, player_row, player_col)
#     if 0 > player_row:
#         player_row = player_row % size
#     if 0 > player_col:
#         player_col = player_col % size
#     if player_row >= size:
#         player_row = player_row % size
#     if player_col >= size:
#         player_col = player_col % size
#     path.append([player_row, player_col])
#     if matrix[player_row][player_col].isdigit():
#         coins += int(matrix[player_row][player_col])
#         matrix[player_row][player_col] = "*"
#     if matrix[player_row][player_col] == "X":
#         coins //= 2
#         break
#     if coins >= 100:
#         break
#
#
# if coins >= 100:
#     print(f"You won! You've collected {coins} coins.")
# else:
#     print(f"Game over! You've collected {coins} coins.")
# print(f"Your path:")
# [print(x)for x in path]