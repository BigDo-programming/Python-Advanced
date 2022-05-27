import sys
from io import StringIO
from pprint import pprint

input1 = """3 4
A B B D
E B B B
I J B B"""

input2 = """5 4
A A B D
A A B B
I J B B
C C C G
C C K P"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

matrix = []
count = 0
n, m = [int(x) for x in input().split()]
for i in range(n):
    value = input().split()
    matrix.append(value)

for row_index in range(n - 1):
    for col_index in range(m - 1):
        if matrix[row_index][col_index] == matrix[row_index][col_index + 1] == \
                matrix[row_index + 1][col_index] == matrix[row_index + 1][col_index + 1]:
            count += 1

print(count)

# def make_matrix():
#     new_matrix = []
#     n, m = [int(x) for x in input().split()]
#     for _ in range(n):
#         value = [x for x in input().split()]
#         new_matrix.append(value)
#     return new_matrix
#
#
# matrix = make_matrix()
# cont = 0
# for r in range(len(matrix) - 1):
#     for c in range(len(matrix[0]) - 1):
#         if matrix[r][c] == matrix[r + 1][c] == matrix[r][c + 1] == matrix[r + 1][c + 1]:
#             cont += 1
#
# print(cont)
