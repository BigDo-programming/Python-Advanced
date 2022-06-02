import sys
from io import StringIO

input1 = """Hello
Bye"""

input2 = """Hello
2"""
# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

text = input()
try:
    num = int(input())
    print(text * num)
except ValueError:
    print("Variable times must be an integer")
