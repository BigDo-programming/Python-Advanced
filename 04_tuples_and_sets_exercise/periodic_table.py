import sys
from io import StringIO

input1 = """4
Ce O
Mo O Ce
Ee
Mo"""


input2 = """3
Ge Ch O Ne
Nb Mo Tc
O Ne"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

set1 = set()

n = int(input())
for i in range(n):
    [set1.add(x) for x in input().split()]
[print(x) for x in set1]


# unique_elements = set()
# n = int(input())
# for i in range(n):
#     [unique_elements.add(x) for x in input().split()]
# [print(x) for x in unique_elements]