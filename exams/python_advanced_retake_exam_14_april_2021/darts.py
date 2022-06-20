import sys
from io import StringIO
from pprint import pprint

input1 = """Ivan, Peter
12 21 18 4 20 7 11
9 D D D D D 10
15 D T T T D 3
2 D T B T D 19
17 D T T T D 6
22 D D D D D 14
5 8 23 13 16 1 24
(3, 3)"""

input2 = """George, Hristo
17 8 21 6 13 3 24
16 D D D D D 14
7 D T T T D 15
23 D T B T D 2
9 D T T T D 22
19 D D D D D 10
12 18 4 20 5 11 1
(1, 0)
(2, 3)
(0, 0)
(4, 2)
(5, 1)
(3, 1)
(0, 0)
(2, 3)"""


# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)



import re


def is_valid(s_row, s_col, s_size):
    return 0 <= s_row < s_size and 0 <= s_col < s_size


def is_turn(t_score, t_matrix, t_row, t_col):
    if t_matrix[t_row][t_col].isdigit():
        t_score -= int(t_matrix[t_row][t_col])

    if t_matrix[t_row][t_col] == 'D':
        t_score -= (int(t_matrix[0][t_col]) + int(t_matrix[-1][t_col]) + int(t_matrix[t_row][-1]) + int(
            t_matrix[t_row][0]))*2

    if t_matrix[t_row][t_col] == 'T':
        t_score -= (int(t_matrix[0][t_col]) + int(t_matrix[-1][t_col]) + int(t_matrix[t_row][-1]) + int(
            t_matrix[t_row][0])) * 3

    if t_matrix[t_row][t_col] == 'B':
        t_score -= 501

    return t_score, t_matrix


size = 7
turn = 0
player1_score = 501
player2_score = 501
winner = False
win = ''
player_one, player_two = input().split(', ')

matrix = []
for _ in range(size):
    value = input().split()
    matrix.append(value)

while player1_score >= 0 or player2_score >= 0:

    if winner:
        break
    turn += 1

    command = input()
    shot_row, shot_col = [int(x) for x in re.findall(r'\d+', command)]
    if is_valid(shot_row, shot_col, size):
        player1_score, matrix = is_turn(player1_score, matrix, shot_row, shot_col)
        if player1_score <= 0:
            winner = True
            win = player_one
            break

    command = input()
    shot_row, shot_col = [int(x) for x in re.findall(r'\d+', command)]

    if is_valid(shot_row, shot_col, size):
        player2_score, matrix = is_turn(player2_score, matrix, shot_row, shot_col)
        if player2_score <= 0:
            winner = True
            win = player_two
            break

print(f"{win} won the game with {turn} throws!")

# import re
#
# size = 7
# matrix = []
#
# player1_score = 501
# player1_throws = 0
# player2_score = 501
# player2_throws = 0
#
# game_win = ''
#
# player1, player2 = input().split(", ")
# for r in range(size):
#     value = input().split()
#     matrix.append(value)
#
# win = False
#
#
# def player_play(row, col, matrix, player_score):
#     if matrix[row][col] == "B":
#         player_score = 510
#     elif matrix[row][col].isdigit():
#         player_score = int(matrix[row][col])
#     elif matrix[row][col] == "D":
#         player_score = (int(matrix[0][col]) + int(matrix[-1][col]) + int(matrix[row][0]) + int(matrix[row][-1])) * 2
#     elif matrix[row][col] == "T":
#         player_score = (int(matrix[0][col]) + int(matrix[-1][col]) + int(matrix[row][0]) + int(matrix[row][-1])) * 3
#     return player_score
#
#
# while True:
#
#     if win:
#         break
#
#     for i in range(1, 2 + 1):
#         command = input()
#         # row, col = [int(x) for x in command if x.isdigit()]
#         # row, col = [int(x) for x in re.findall(r"\d+", command)]
#         row, col = [int(x) for x in re.findall(r"-*\d+|\d+", command)]
#
#         if 0 <= row < size and 0 <= col < size:
#
#             if i == 1:
#                 player1_score -= player_play(row, col, matrix, player1_score)
#                 player1_throws += 1
#
#                 if player1_score <= 0:
#                     game_win = player1
#                     win = True
#                     break
#             elif i == 2:
#                 player2_score -= player_play(row, col, matrix, player1_score)
#                 player2_throws += 1
#
#                 if player2_score <= 0:
#                     game_win = player2
#                     win = True
#                     break
#
#         else:
#             continue
#
# throws = player1_throws if game_win == player1 else player2_throws
# print(f"{game_win} won the game with {throws} throws!")


