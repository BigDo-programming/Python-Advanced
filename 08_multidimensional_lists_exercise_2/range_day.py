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
sys.stdin = StringIO(input1)

targets = 0
player_row, player_col = 0, 0
matrix = []
for r in range(5):
    value = [x for x in input().split()]
    matrix.append(value)
    for c in range(5):
        if value[c] == "A":
            player_row, player_col = r, c
        elif value[c] == "x":
            targets += 1

pprint(matrix)
print(targets)
n = int(input())
for i in range(n):
    data = input().split()
    if data[0] == "move":
        pass
    else:
        pass