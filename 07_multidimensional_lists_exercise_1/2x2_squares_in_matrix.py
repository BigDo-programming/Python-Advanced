import sys
from io import StringIO

input1 = """3 4
A B B D
E B B B
I J B B"""

sys.stdin = StringIO(input1)

matrix = []
n, m = [int(x) for x in input().split()]
for i in range(n):
    value = [x for x in input().split()]
    matrix.append(value)

count = 0

for r in range(n-1):
    for c in range(m-1):
        if matrix[r][c] == matrix[r][c+1] == matrix[r+1][c] == matrix[r+1][c+1]:
            count += 1
print(count)
