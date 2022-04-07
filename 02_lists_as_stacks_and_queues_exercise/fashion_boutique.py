import sys
from io import StringIO

input1 = """5 4 8 6 3 8 7 7 9
16"""
input2 = """1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
20"""
input3 = """"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

clothes = [int(x) for x in input().split()]
capacity = int(input())
boxes = 0
clothes_sum = 0
while clothes:
    if clothes_sum + clothes[-1] <= capacity:
        clothes_sum += clothes.pop()
    else:
        boxes += 1
        clothes_sum = 0

if clothes_sum:
    boxes += 1
print(boxes)