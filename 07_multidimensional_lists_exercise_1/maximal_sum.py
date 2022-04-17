import sys
from io import StringIO

input1 = """4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4"""

sys.stdin = StringIO(input1)

matrix = []
n, m = [int(x) for x in input().split()]
for i in range(n):
    value = [int(x) for x in input().split()]
    matrix.append(value)
