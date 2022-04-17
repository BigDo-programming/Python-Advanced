import sys
from io import StringIO

input1 = """4
-7 14 9 -20
3 4 9 21
-14 6 8 44
30 9 7 -14"""

sys.stdin = StringIO(input1)

matrix = []
n = int(input())
for i in range(n):
    value = [int(x) for x in input().split()]
    matrix.append(value)


primary_diagonal = 0
secondary_diagonal = 0
for c in range(n):
    primary_diagonal += matrix[c][c]
    secondary_diagonal += matrix[c][n - 1 - c]

print(abs(primary_diagonal - secondary_diagonal))
