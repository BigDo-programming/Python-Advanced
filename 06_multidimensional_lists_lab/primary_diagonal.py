import sys
from io import StringIO

input1 = """3
11 2 4
4 5 6
10 8 -12"""

sys.stdin = StringIO(input1)

matrix = []

n = int(input())
for row_index in range(n):
    value = [int(x) for x in input().split()]
    matrix.append(value)

primary_sum = 0
for i in range(n):
    primary_sum += matrix[i][i]

print(primary_sum)

# def read_matrix():
#     n = int(input())
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
# n = len(matrix)
# print(sum(matrix[i][i] for i in range(n)))


# n = int(input())
# matrix = []
# for i in range(n):
#     value = [int(x) for x in input().split()]
#     matrix.append(value)

# primary_diagonal_sum = 0
# for i in range(n):
#     primary_diagonal_sum += matrix[i][i]
#
# print(primary_diagonal_sum)

# print(sum([matrix[i][i] for i in range(n)]))
