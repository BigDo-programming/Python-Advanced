import sys
from io import StringIO

input1 = """5 
0K0K0
K000K
00K00
K000K
0K0K0"""

input2 = """2
KK
KK"""

input3 = """8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)


def how_many_knights_attack(row, col, matrix):
    count = 0
    if 0 <= row - 2 < len(matrix) and 0 <= col - 1 < len(matrix):
        if matrix[row - 2][col - 1] == "K":
            count += 1

    if 0 <= row - 1 < len(matrix) and 0 <= col - 2 < len(matrix):
        if matrix[row - 1][col - 2] == "K":
            count += 1

    if 0 <= row + 1 < len(matrix) and 0 <= col - 2 < len(matrix):
        if matrix[row + 1][col - 2] == "K":
            count += 1

    if 0 <= row + 2 < len(matrix) and 0 <= col - 1 < len(matrix):
        if matrix[row + 2][col - 1] == "K":
            count += 1

    if 0 <= row - 2 < len(matrix) and 0 <= col + 1 < len(matrix):
        if matrix[row - 2][col + 1] == "K":
            count += 1

    if 0 <= row - 1 < len(matrix) and 0 <= col + 2 < len(matrix):
        if matrix[row - 1][col + 2] == "K":
            count += 1

    if 0 <= row + 1 < len(matrix) and 0 <= col + 2 < len(matrix):
        if matrix[row + 1][col + 2] == "K":
            count += 1

    if 0 <= row + 2 < len(matrix) and 0 <= col + 1 < len(matrix):
        if matrix[row + 2][col + 1] == "K":
            count += 1
    return count


matrix = []

n = int(input())
for _ in range(n):
    value = list(input())
    matrix.append(value)

removed_knights = 0
while True:
    best_knights = 0
    best_col = 0
    best_row = 0

    for i in range(n):
        for j in range(n):

            if matrix[i][j] == "0":
                continue
            numbers = how_many_knights_attack(i, j, matrix)
            if numbers > best_knights:
                best_knights = numbers
                best_row = i
                best_col = j

    if best_knights == 0:
        break

    matrix[best_row][best_col] = "0"
    removed_knights += 1

print(removed_knights)

#
# def is_inside(row, col, n):
#     return 0 <= row < n and 0 <= col < n
#
#
# def is_knight(row, col, matrix):
#     return matrix[row][col] == "K"
#
#
# def get_attack_counter(row, col, matrix):
#     result = 0
#     if is_inside(row - 2, col - 1, len(matrix)) and is_knight(row - 2, col - 1, matrix):
#         result += 1
#     if is_inside(row - 2, col + 1, len(matrix)) and is_knight(row - 2, col + 1, matrix):
#         result += 1
#     if is_inside(row - 1, col - 2, len(matrix)) and is_knight(row - 1, col - 2, matrix):
#         result += 1
#     if is_inside(row - 1, col + 2, len(matrix)) and is_knight(row - 1, col + 2, matrix):
#         result += 1
#     if is_inside(row + 2, col - 1, len(matrix)) and is_knight(row + 2, col - 1, matrix):
#         result += 1
#     if is_inside(row + 2, col + 1, len(matrix)) and is_knight(row + 2, col + 1, matrix):
#         result += 1
#     if is_inside(row + 1, col - 2, len(matrix)) and is_knight(row + 1, col - 2, matrix):
#         result += 1
#     if is_inside(row + 1, col + 2, len(matrix)) and is_knight(row + 1, col + 2, matrix):
#         result += 1
#     return result
#
#
# matrix = []
# n = int(input())
# for i in range(n):
#     value = list(input())
#     matrix.append(value)
#
# removed_knight = 0
#
# while True:
#     table = {}
#
#     for row in range(n):
#         for col in range(n):
#             if matrix[row][col] == "0":
#                 continue
#
#             counter = get_attack_counter(row, col, matrix)
#             if counter > 0:
#                 table[(row, col)] = counter
#
#     if len(table) == 0:
#         break
#
#     best_counter = 0
#     knight_row, knight_col = 0, 0
#     for coords, counter in table.items():
#         if counter > best_counter:
#             best_counter = counter
#             knight_row = coords[0]
#             knight_col = coords[1]
#     matrix[knight_row][knight_col] = "0"
#     removed_knight += 1
#
# print(removed_knight)
