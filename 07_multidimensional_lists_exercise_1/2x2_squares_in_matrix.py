import sys
from io import StringIO

input1 = """3 4
A B B D
E B B B
I J B B"""

sys.stdin = StringIO(input1)























#
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
