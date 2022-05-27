import sys
from io import StringIO

input1 = """3
1, 2, 3
4, 5, 6
7, 8, 9"""

sys.stdin = StringIO(input1)

matrix = []
primary_diagonal = []
secondary_diagonal = []
n = int(input())
for i in range(n):
    value = [int(x) for x in input().split(", ")]
    matrix.append(value)
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][n - i - 1])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

# def make_matrix():
#     new_matrix = []
#     n = int(input())
#     for _ in range(n):
#         value = [int(x) for x in input().split(", ")]
#         new_matrix.append(value)
#     return new_matrix
#
#
# matrix = make_matrix()
# primary_diagonal = []
# secondary_diagonal = []
#
# for i in range(len(matrix)):
#     primary_diagonal.append(matrix[i][i])
#     secondary_diagonal.append(matrix[i][len(matrix) - 1 - i])
#
# print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

# matrix = []
# primary_diagonal = []
# secondary_diagonal = []
#
# n = int(input())
# for i in range(n):
#     value = [int(x) for x in input().split(", ")]
#     matrix.append(value)
#
# for r in range(n):
#     primary_diagonal.append(matrix[r][r])
#     secondary_diagonal.append(matrix[r][n - 1 - r])
#
# print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
