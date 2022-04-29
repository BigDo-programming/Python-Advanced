import sys
from io import StringIO
from pprint import pprint

input1 = """Hello
4
P---
Mark
-l-y
--e-
4
down
right
right
right"""

input2 = """Initial
5
-----
t-r--
--Pa-
--S--
z--t-
4
up
left
left
left"""

input3 = """I
5
-----
t-r--
--Pa-
--S--
z--t-
4
left
left
left
left"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)


def move(r, c, command):
    if command == "up":
        return r - 1, c
    if command == "down":
        return r + 1, c
    if command == "left":
        return r, c - 1
    if command == "right":
        return r, c + 1


text = list(input())
size = int(input())
matrix = []
player_r = 0
player_c = 0
for r in range(size):
    value = list(input())
    matrix.append(value)
    for c in range(size):
        if matrix[r][c] == "P":
            player_r, player_c = r, c
            matrix[player_r][player_c] = "-"

n = int(input())
end_row = player_r
end_col = player_c
for _ in range(n):
    command = input()
    player_r, player_c = move(player_r, player_c, command)
    if 0 <= player_r < len(matrix) and 0 <= player_c < len(matrix):
        end_row, end_col = player_r, player_c
        char = str(matrix[player_r][player_c])
        if char.isalpha():
            text.append(char)
            matrix[player_r][player_c] = "-"

    else:
        if text:
            text.pop()

matrix[end_row][end_col] = "P"

print(*text, sep="")
[print(*x, sep="") for x in matrix]
# ToDo 90/100
