import sys
from io import StringIO

input1 = """Tom, Jerry
. . T . . .
. . . . . .
. . W . . .
. . W . . E
. . . . . .
. T . W . .
(3, 2)
(1, 3)
(5, 1)
(5, 1)"""

input2 = """Jerry, Tom
. T . . . W
. . . . T .
. W . . . T
. T . E . .
. . . . . T
. . T . . .
(1, 1)
(3, 0)
(3, 3)"""

input3 = """Jerry, Tom
. . . W . .
. . T T . .
. . . . . .
. T . W . .
W . . . E .
. . . W . .
(0, 3)
(3, 3)
(1, 3)
(2, 2)
(3, 5)
(4, 0)
(5, 3)
(3, 1)
(4, 4)
(4, 4)"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

import re

first_player, second_player = input().split(', ')
first_player_wall = 0
second_player_wall = 0
size = 6
matrix = []
winner = None
m_row, m_col = 0, 0
for r in range(size):
    value = input().split()
    matrix.append(value)

while True:
    for i in range(1, 2 + 1):
        if i == 1:
            first_player_row, first_player_col = [int(x) for x in re.findall(r'\d+', input())]
            if first_player_wall > 0:
                first_player_wall -= 1
                continue

            if matrix[first_player_row][first_player_col] == 'E':
                winner = first_player
                print(f"{first_player} found the Exit and wins the game!")
                exit()

            if matrix[first_player_row][first_player_col] == 'T':
                winner = second_player
                print(f"{first_player} is out of the game! The winner is {winner}.")
                exit()

            if matrix[first_player_row][first_player_col] == 'W':
                first_player_wall += 1
                print(f"{first_player} hits a wall and needs to rest.")
        else:
            second_player_row, second_player_col = [int(x) for x in re.findall(r'\d+', input())]
            if second_player_wall > 0:
                second_player_wall -= 1
                continue

            if matrix[second_player_row][second_player_col] == 'E':
                winner = second_player
                print(f"{second_player} found the Exit and wins the game!")
                exit()

            if matrix[second_player_row][second_player_col] == 'T':
                winner = first_player
                print(f"{second_player} is out of the game! The winner is {winner}.")
                exit()

            if matrix[second_player_row][second_player_col] == 'W':
                second_player_wall += 1
                print(f"{second_player} hits a wall and needs to rest.")
