import sys
from io import StringIO

input1 = """6
George
George
George
Peter
George
NiceGuy1234"""

sys.stdin = StringIO(input1)

unique_usernames = set()
n = int(input())
for _ in range(n):
    name = input()
    unique_usernames.add(name)
[print(x) for x in unique_usernames]
