from cgitb import reset
from os import name
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


n = int(input())
names = {input() for _ in range(n)}
[print(name) for name in names]