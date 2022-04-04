import sys
from io import StringIO

input1 = """9
1 97
2
1 20
2
1 26
1 20
3
1 91
4"""
input2 = """"""
input3 = """"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


stack = []
n = int(input())
for i in range(n):
    data = input()
    data_split = data.split()
    action = data_split[0]
    if action == "1":
        number = data_split[1]
        stack.append(number)
    elif action == "2":
        stack.pop()
    elif action == "3":
        print(max(stack))
    elif action == "4":
        print(min(stack))

while stack:
    print(" ".join(stack.pop()))
