import sys
from io import StringIO

input1 = """4 3
1
3
5
7
3
4
5"""

sys.stdin = StringIO(input1)

set1 = set()
set2 = set()

m_n = input().split()
n = int(m_n[0])
m = int(m_n[1])
for _ in range(n):
    set1.add(input())
for _ in range(m):
    set2.add(input())
set3 = set1.intersection(set2)
[print(x) for x in set3]
