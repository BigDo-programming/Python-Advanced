import sys
from io import StringIO
from pprint import pprint

input1 = """Ivan, Peter
12 21 18 4 20 7 11
9 D D D D D 10
15 D T T T D 3
2 D T B T D 19
17 D T T T D 6
22 D D D D D 14
5 8 23 13 16 1 24
(3, 3)"""

input2 = """George, Hristo
17 8 21 6 13 3 24
16 D D D D D 14
7 D T T T D 15
23 D T B T D 2
9 D T T T D 22
19 D D D D D 10
12 18 4 20 5 11 1
(1, 0)
(2, 3)
(0, 0)
(4, 2)
(5, 1)
(3, 1)
(0, 0)
(2, 3)"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

size = 7
matrix = []
player1, player2 = input().split()
player1_score = 501
player2_score = 501
for r in range(size):
    value = input().split()
    matrix.append(value)
pprint(matrix)