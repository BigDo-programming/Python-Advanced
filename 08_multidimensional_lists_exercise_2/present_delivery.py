import sys
from io import StringIO
from pprint import pprint

input1 = """5
4
- X V -
- S - V
- - - -
X - - -
up
right
down
right
Christmas morning"""
input2 = """3
4
- - - -
V - X -
- V C V
- - - S
left
up"""
input3 = """"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)


def move_santa(s_row, s_col, direction):
    if direction == "up":
        return s_row - 1, s_col
    if direction == "down":
        return s_row + 1, s_col
    if direction == "left":
        return s_row, s_col - 1
    if direction == "right":
        return s_row, s_col + 1


number_of_santa_presents = int(input())
presents = 0
good_kids = 0
size = int(input())
santa_row, santa_col = 0, 0
matrix = []
for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "S":
            santa_row, santa_col = row, col
        if matrix[row][col] == "V":
            good_kids += 1

pprint(matrix)
matrix[santa_row][santa_col] = "-"
while True:
    command = input()
    if number_of_santa_presents == 0:
        break
    if command == "Christmas morning":
        break
    santa_row, santa_col = move_santa(santa_row, santa_col, command)
    if matrix[santa_row][santa_col] == "V":
        presents += 1
        matrix[santa_row][santa_col] = "-"
matrix[santa_row][santa_col] = "S"

pprint(matrix)
if number_of_santa_presents == 0 and good_kids > presents:
    print(f"Santa ran out of presents!")
if good_kids == presents:
    print(f"Good job, Santa! {presents} happy nice kid/s.")