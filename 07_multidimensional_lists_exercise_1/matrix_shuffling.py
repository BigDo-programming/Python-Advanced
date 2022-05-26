import sys
from io import StringIO

input1 = """2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7 
swap 0 1 1 0
END"""

input2 = """1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END"""

sys.stdin = StringIO(input1)


































# def is_valid(r, c, row, col):
#     return 0 <= row < r and 0 <= col < c
#
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
#
# command = input()
# while not command == "END":
#     command_split = command.split()
#     if not command_split[0] == 'swap' or not len(command_split[1:]) == 4:
#         print("Invalid input!")
#
#     else:
#         row1, col1, row2, col2 = [int(x) for x in command_split[1:]]
#         if is_valid(len(matrix), len(matrix[0]), row1, col1) and is_valid(len(matrix), len(matrix[0]), row2, col2):
#             matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#             for row in matrix:
#                 [print(x, end=" ") for x in row]
#                 print()
#         else:
#             print("Invalid input!")
#
#     command = input()

# def is_valid(r, c, rows, cols):
#     return 0 <= r < rows or 0 <= r < cols
#
#
# n, m = [int(x) for x in input().split()]
# matrix = []
# for r in range(n):
#     value = [x for x in input().split()]
#     matrix.append(value)
#
# while True:
#     command = input()
#     if command == "END":
#         break
#
#     command_split = command.split()
#
#     if len(command_split) != 5 or command_split[0] != 'swap':
#         print("Invalid input!")
#         continue
#
#     row1, col1, row2, col2 = [int(x) for x in command_split[1:]]
#     if not is_valid(row1, col1, n, m) or not is_valid(row2, col2, n, m):
#         print("Invalid input!")
#         continue
#
#     matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#     for row_elements in matrix:
#         print(' '.join([str(x) for x in row_elements]))
