import sys
from io import StringIO
from pprint import pprint

input1 = """10 30 B 4 20 24
7 8 27 23 11 19
13 3 14 B 17 В
12 5 21 22 9 6
B 26 1 28 29 2
25 B 16 15 B 18
(1, 1)
(20, 15)
(4, 0)"""

input2 = """B 30 14 23 20 24
29 8 27 18 11 19
13 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)"""

input3 = """"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)
import re


def prizes(points):
    if 100 <= points <= 199:
        return f"Good job! You scored {points} points, and you've won Football."

    elif 200 <= points <= 299:
        return f"Good job! You scored {points} points, and you've won Teddy Bear."

    elif points >= 300:
        return f"Good job! You scored {points} points, and you've won Lego Construction Set."

    else:
        return f"Sorry! You need {abs(points - 100)} points more to win a prize."


matrix = []
size = 6
sum_of_the_points = 0
for row in range(size):
    value = input().split()
    matrix.append(value)
for _ in range(3):
    throw = input()
    throw_row, throw_col = [int(x) for x in re.findall(r"\d+", throw)]
    if 0 <= throw_row < size and 0 <= throw_col < size and matrix[throw_row][throw_col] == "B":
        matrix[throw_row][throw_col] = "*"

        for r in range(size):
            if matrix[r][throw_col].isdigit():
                sum_of_the_points += int(matrix[r][throw_col])

print(prizes(sum_of_the_points))

# import re
#
# size = 6
# score = 0
# matrix = []
# for row in range(size):
#     # value = [int(x) if x.isdigit() else str(x) for x in input().split()]
#     value = input().split()
#     matrix.append(value)
#
# for _ in range(3):
#     command = input()
#     shot_row, shot_col = [int(x) for x in re.findall(r'\d+', command)]
#     if 0 <= shot_row < size and 0 <= shot_col < size:
#         if matrix[shot_row][shot_col] == 'B':
#             matrix[shot_row][shot_col] = '0'
#             for i in range(size):
#                 if matrix[i][shot_col].isdigit():
#                     score += int(matrix[i][shot_col])
#
# prize = ''
# if 100 <= score <= 199:
#     prize = 'Football'
# elif 200 <= score <= 299:
#     prize = 'Teddy Bear'
# elif 300 <= score:
#     prize = 'Lego Construction Set'
#
# if prize:
#     print(f"Good job! You scored {score} points, and you've won {prize}.")
# else:
#     print(f"Sorry! You need {100 -score} points more to win a prize.")