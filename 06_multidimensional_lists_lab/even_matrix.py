import sys
from io import StringIO

input1 = """4
10, 33, 24, 5, 1
67, 34, 11, 110, 3
4, 12, 33, 63, 21
557, 45, 23, 55, 67"""

sys.stdin = StringIO(input1)

matrix = []

n = int(input())
for _ in range(n):
    value = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(value)

print(matrix)

# def read_matrix():
#     n = int(input())
#
#     matrix = []
#
#     for _ in range(n):
#         row = [int(x) for x in input().split(', ') ]
#         matrix.append(row)
#
#     return(matrix)
#
#
# matrix = read_matrix()
# even_matrix = []
# for row in matrix:
#     only_even = [x for x in row if x % 2 == 0]
#     even_matrix.append(only_even)
# print(even_matrix)

# matrix = []
# n = int(input())
# for i in range(n):
#     row = map(int, input().split(', '))
#     even_row = [x for x in row if x % 2 == 0]
#     matrix.append(even_row)
#
# print(matrix)
