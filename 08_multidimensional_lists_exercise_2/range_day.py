import sys
from io import StringIO
from pprint import pprint

input1 = """. . . . .
x . . . .
. A . . .
. . . x .
. x . . x
3
shoot down
move right 4
move left 1"""

input2 = """. . . . .
. . . . .
. A x . .
. . . . .
. x . . .
2
shoot down
shoot right"""

input3 = """. . . . .
. . . . .
. . x . .
. . . . .
. x . . A
3
shoot down
move right 2
shoot left"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)


def go_to(row, col, command, steps=1):
    if command == "up":
        return row - steps, col
    elif command == "down":
        return row + steps, col
    elif command == "left":
        return row, col - steps
    elif command == "right":
        return row, col + steps


def is_outside(row_, col_, n):
    return row_ < 0 or col_ < 0 or row_ >= n or col_ >= n


matrix = []
hit_target = []
player_row = 0
player_col = 0

targets = 0
size = 5
for i in range(size):
    value = input().split()
    matrix.append(value)
    for j in range(size):
        if matrix[i][j] == "A":
            player_row, player_col = i, j
        elif matrix[i][j] == "x":
            targets += 1

firsts_targets = targets
matrix[player_row][player_col] = "."
n = int(input())

for _ in range(n):
    if targets == 0:
        break
    command = input().split()

    if command[0] == "shoot":
        bullet_row, bullet_col = player_row, player_col

        while True:
            bullet_row, bullet_col = go_to(bullet_row, bullet_col, command[1])
            if is_outside(bullet_row, bullet_col, size):
                break
            elif matrix[bullet_row][bullet_col] == ".":
                continue
            elif matrix[bullet_row][bullet_col] == "x":
                matrix[bullet_row][bullet_col] = "."
                hit_target.append([bullet_row, bullet_col])
                targets -= 1
                break

    elif command[0] == "move":

        try_row, try_col = player_row, player_col
        try_row, try_col = go_to(try_row, try_col, command[1], int(command[2]))
        if is_outside(try_row, try_col, size):
            continue
        elif not matrix[try_row][try_col] == ".":
            continue
        else:
            player_row, player_col = try_row, try_col
            matrix[player_row][player_col] = "."

if not targets:
    print(f"Training completed! All {firsts_targets} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")
[print(x) for x in hit_target]

# def is_outside(row, col, size):
#     return row < 0 or col < 0 or row >= size or col >= size
#
#
# def get_next_pos(d, r, c, steps):
#     if d == "up":
#         return r - steps, c
#     if d == "down":
#         return r + steps, c
#     if d == "left":
#         return r, c - steps
#     if d == "right":
#         return r, c + steps
#
#
# size = 5
# targets = 0
#
# player_row = 0
# player_col = 0
# matrix = []
# for r in range(size):
#     value = [x for x in input().split()]
#     matrix.append(value)
#     for c in range(5):
#         if value[c] == "A":
#             player_row, player_col = r, c
#         elif value[c] == "x":
#             targets += 1
#
# n = int(input())
# targets_left = targets
# hit_targets = []
# for i in range(n):
#     data = input().split()
#     command = data[0]
#     directions_to_move_and_shoot = data[1]
#
#     if command == "move":
#         steps = int(data[2])
#         next_row, next_col = get_next_pos(directions_to_move_and_shoot, player_row, player_col, steps)
#
#         if is_outside(next_row, next_col, size) or matrix[next_row][next_col] != ".":
#             continue
#         matrix[player_row][player_col] = "."
#         player_row, player_col = next_row, next_col
#         matrix[player_row][player_col] = "A"
#
#     else:
#         bullet_row, bullet_col = player_row, player_col
#         while True:
#             bullet_row, bullet_col = get_next_pos(directions_to_move_and_shoot, bullet_row, bullet_col, 1)
#             if is_outside(bullet_row, bullet_col, size):
#                 break
#             if matrix[bullet_row][bullet_col] == "x":
#                 hit_targets.append([bullet_row, bullet_col])
#                 matrix[bullet_row][bullet_col] = "."
#                 targets_left -= 1
#
#                 break
#         if targets_left == 0:
#             break
#
# if targets_left == 0:
#     print(f"Training completed! All {targets} targets hit.")
# else:
#     print(f"Training not completed! {targets_left} targets left.")
# for target in hit_targets:
#     print(target)
