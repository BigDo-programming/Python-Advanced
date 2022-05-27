import sys
from io import StringIO
from pprint import pprint

input1 = """5 6
SoftUni"""
input2 = """1 4
Python"""

sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

n, m = [int(x) for x in input().split()]
word = input()
count = 0
matrix = []
for _ in range(n):
    matrix.append([0] * m)

for i in range(n):

    if i % 2 == 0:
        for j in range(m):
            matrix[i][j] = word[count]
            count = (count + 1) % len(word)
    else:
        for j in range(m - 1, -1, -1):
            matrix[i][j] = word[count]
            count = (count + 1) % len(word)

for ch in matrix:
    print(*ch, sep="")

# n, m = [int(x) for x in input().split()]
# word = input()
#
#
# matrix = []
# for i in range(n):
#     matrix.append([None] * m)
#
# count = 0
# for r in range(len(matrix)):
#     for c in range(len(matrix[0])):
#         if r % 2 == 0:
#             matrix[r][c] = word[count]
#         else:
#             matrix[r][m - 1 - c] = word[count]  # 6 - 1 - 1 = 5 - движи редът от зад на пред
#         count = (count + 1) % len(word) # каунтър който се върти по текста (като стигне до последната - дели и дава 0)
#
# # pprint(matrix)
# for elements in matrix:
#     print(''.join(elements))
#


# n, m = [int(x) for x in input().split()]
# word = input()
# matrix = []
# word_index = 0
#
# for row in range(n):
#     matrix.append([None] * m)
#     for col in range(m):
#         if row % 2 == 0:
#             matrix[row][col] = word[word_index]
#         else:
#             matrix[row][m - 1 - col] = word[word_index]
#
#         word_index = (word_index + 1) % len(word)

# for elements in matrix:
#     print(''.join(elements))
