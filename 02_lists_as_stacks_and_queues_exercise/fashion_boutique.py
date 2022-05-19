import sys
from io import StringIO

input1 = """5 4 8 6 3 8 7 7 9
16"""
input2 = """1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
20"""
input3 = """"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)
rack = 0
box_of_clothes = [int(x) for x in input().split()]
capacity_of_one_rack = int(input())
clothe_sum = 0
while box_of_clothes:

    clothe = box_of_clothes.pop()
    if clothe_sum + clothe <= capacity_of_one_rack:
        clothe_sum += clothe

    else:
        rack += 1
        clothe_sum = clothe
if clothe_sum:
    rack += 1
print(rack)

# racks = 0
# box_of_clothes = [int(x) for x in input().split()]
# capacity_one_rack = int(input())
#
# capacity = 0
# while box_of_clothes:
#     if box_of_clothes[-1] + capacity <= capacity_one_rack:
#         capacity += box_of_clothes[-1]
#         box_of_clothes.pop()
#     else:
#         racks += 1
#         capacity = 0
#
# if capacity > 0:
#     racks += 1
# print(racks)
#
