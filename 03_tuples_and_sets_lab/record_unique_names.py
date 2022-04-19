import sys
from io import StringIO

input1 = """8
Lee
Joey
Lee
Joe
Alan
Alan
Peter
Joey"""

sys.stdin = StringIO(input1)

names = set()
n = int(input())
for i in range(n):
    names.add(input())

[print(x) for x in names]

# n = int(input())
# names = {input() for _ in range(n)}
# [print(name) for name in names]
