import sys
from io import StringIO

input1 = """5 6
.....P
......
...B..
......
......
ULDDDR"""
input2 = """4 5
.....
.....
.B...
...P.
LLLLLLLL"""
input3 = """5 8
.......B
...B....
....B..B
........
..P.....
ULLL"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

def get_next_pos(row, col, direction):
    if direction == "U":
        return row - 1, col
    elif direction == "D":
        return row + 1, col
    elif direction == "L":
        return row, col - 1
    elif direction == "R":
        return row, col + 1


def is_outside(n_row, n_col, n, m):
    return 0 > n_row or 0 > n_col or n_row >= n or n_col >= m


def get_children(b_row, b_col, n, m):
    possible_children = [
        [b_row - 1, b_col],
        [b_row + 1, b_col],
        [b_row, b_col - 1],
        [b_row, b_col + 1],
    ]
    result = []
    for child_row, child_col in possible_children:
        if not is_outside(child_row, child_col, n, m):
            result.append([child_row, child_col])
    return result


matrix = []
bunnies = set()
player_row = 0
player_col = 0
n, m = [int(x) for x in input().split()]
for i in range(n):
    value = list(input())
    matrix.append(value)
    for j in range(m):
        if matrix[i][j] == "P":
            player_row, player_col = i, j
        elif matrix[i][j] == "B":
            bunnies.add(f"{i} {j}")

commands = list(input())
won = False
dead = False

for command in commands:
    next_row, next_col = get_next_pos(player_row, player_col, command)
    matrix[player_row][player_col] = "."

    if is_outside(next_row, next_col, n, m):
        won = True
    elif matrix[next_row][next_col] == "B":
        dead = True
        player_row, player_col = next_row, next_col
    else:
        matrix[next_row][next_col] = "P"
        player_row, player_col = next_row, next_col
    new_bunnies = set()
    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]
        children = get_children(bunny_row, bunny_col, n, m)
        for child_row, child_col in children:
            new_bunnies.add(f"{child_row} {child_col}")
            matrix[child_row][child_col] = "B"
            if child_row == player_row and child_col == player_col:
                dead = True
    bunnies = bunnies.union(new_bunnies)
    if won or dead:
        break

[print(*x, sep="") for x in matrix]
if won:
    print(f"won: {player_row} {player_col}")
if dead:
    print(f"dead: {player_row} {player_col}")
# ToDo 70/100