import sys
from io import StringIO

input1 = """1 2 3 |4 5 6 |  7  88"""

sys.stdin = StringIO(input1)

sublist = input().split("|")
result = []
for index in range(len(sublist) - 1, -1, -1):
    elements = sublist[index].split()
    print(*elements, end=" ")
