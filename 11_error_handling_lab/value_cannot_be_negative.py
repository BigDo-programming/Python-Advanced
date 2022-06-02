import sys
from io import StringIO

input1 = """1
4
-5
3
10"""

sys.stdin = StringIO(input1)


class ValueCannotBeNegative(Exception):
    pass


n = 5
for _ in range(n):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative

