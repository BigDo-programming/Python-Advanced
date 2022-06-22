import sys
from io import StringIO

input1 = """"""

input2 = """"""

input3 = """"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


from collections import deque

tests = deque([int(x) for x in input().split()])
tests1 = [int(x) for x in input().split()]

while tests1 or tests:
    if not tests:
        break

    if not tests1:
        break

