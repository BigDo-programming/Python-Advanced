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
sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)


snake_row = 0
snake_col = 0
size = int(input())
matrix = []
for r in range(size):
    value = list(input())
    matrix.append(value)
    for c in range(size):
        if value[c] == 'S':
            snake_row, snake_col = r, c
pprint(matrix)
print(snake_row, snake_col)
