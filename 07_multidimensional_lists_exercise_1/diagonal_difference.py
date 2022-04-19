import sys
from io import StringIO

input1 = """4
-7 14 9 -20
3 4 9 21
-14 6 8 44
30 9 7 -14"""

sys.stdin = StringIO(input1)


def make_matrix():
    new_matrix = []
    n = int(input())
    for _ in range(n):
        value = [int(x) for x in input().split()]
        new_matrix.append(value)
    return new_matrix


matrix = make_matrix()
primary_diagonal = 0
secondary_diagonal = 0

for i in range(len(matrix)):
    primary_diagonal += matrix[i][i]
    secondary_diagonal += matrix[i][len(matrix) - 1 - i]

print(abs(primary_diagonal-secondary_diagonal))





# matrix = []
# n = int(input())
# for _ in range(n):
#     value = [int(x) for x in input().split()]
#     matrix.append(value)
#
#
# primary_diagonal = 0
# secondary_diagonal = 0
#
# for i in range(n):
#     primary_diagonal += matrix[i][i]
#     secondary_diagonal += matrix[i][n - 1 - i]
#
#     # print(matrix[i][len(matrix) - 1 - i])
#     # print(matrix[len(matrix) - 1 - i][i])
#
#
#
# print(abs(primary_diagonal - secondary_diagonal))
