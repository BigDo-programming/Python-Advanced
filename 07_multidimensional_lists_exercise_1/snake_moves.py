import sys
from io import StringIO

input1 = """5 6
SoftUni"""

sys.stdin = StringIO(input1)

n, m = [int(x) for x in input().split()]
word = input()
matrix = []
word_index = 0

for row in range(n):
    matrix.append([None] * m)
    for col in range(m):
        if row % 2 == 0:
            matrix[row][col] = word[word_index]
        else:
            matrix[row][m - 1 - col] = word[word_index]

        word_index = (word_index + 1) % len(word)

for elements in matrix:
    print(''.join(elements))
