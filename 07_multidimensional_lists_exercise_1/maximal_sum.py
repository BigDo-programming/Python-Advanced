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

max_sum = 0
best_col = 0
best_row = 0

for r in range(n - 2):
    for c in range(m - 2):
        current_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] + matrix[r + 1][c] + matrix[r + 1][c + 1] + \
                      matrix[r + 1][c + 2] + matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]
        if current_sum > max_sum:
            max_sum, best_row, best_col = current_sum, r, c

print(f"Sum = {max_sum}")
print(matrix[best_row][best_col], matrix[best_row][best_col + 1], matrix[best_row][best_col + 2])
print(matrix[best_row + 1][best_col], matrix[best_row + 1][best_col + 1], matrix[best_row + 1][best_col + 2])
print(matrix[best_row + 2][best_col], matrix[best_row + 2][best_col + 1], matrix[best_row + 2][best_col + 2])

# Todo 80/1oo
