import sys
from io import StringIO
from pprint import pprint

input1 = """3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0"""

sys.stdin = StringIO(input1)

# def read_matrix():
#     n,m = [int(x) for x in input().split(', ') ]
#     # n,m = map(int, input().split(', ')
#
#     matrix = []
#
#     for _ in range(n):
#         row = [int(x) for x in input().split() ]
#         matrix.append(row)
#
#     return(matrix)
#
#
# matrix = read_matrix()
#
# n = len(matrix)
# m = len(matrix[0])
# column_sums = [0] * m
#
# # for r in range(n):
# #     for c in range(m):
# #         value = matrix[r][c]
# #         column_sums[c] += value
#
# for c in range(m):
#     for r in range(n):
#         value = matrix[r][c]
#         column_sums[c] += value
#
#
# [print(x) for x in column_sums]


# n, m = [int(x) for x in input().split(", ")]
#
# matrix = []
# for i in range(n):
#     row = [int(x) for x in input().split()]
#     matrix.append(row)

# column_sums = [0]*m
# for r in range(n):
#     for c in range(m):
#         value = matrix[r][c]
#         column_sums[c] += value


# for i in range(m):
#     sum_matrix_columns = 0
#     for j in range(n):
#
#         value = matrix[j][i]
#         sum_matrix_columns += value
#
#     print(sum_matrix_columns)
#

n, m = [int(x) for x in input().split(", ")]

matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

col_sum = 0
for c in range(m):
    for r in range(n):
        col_sum += matrix[r][c]
    print(col_sum)
    col_sum = 0
