import sys
from io import StringIO

input1 = """1 2 3 4 5"""
input2 = """"""
input3 = """"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

# my_list = [int(x) for x in input().split()]
# stack = []
# while my_list:
#     stack.append(my_list.pop())
# print(*stack)

my_list = [int(x) for x in input().split()]

while my_list:
    print(my_list.pop(),end=' ')
