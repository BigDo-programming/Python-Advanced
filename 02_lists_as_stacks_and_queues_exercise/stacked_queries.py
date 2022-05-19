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

queries = []
n = int(input())
for _ in range(n):
    data = input().split()

    command = int(data[0])
    if command == 1:
        number = int(data[1])
        queries.append(number)

    if command == 2 and queries:
        queries.pop()

    if command == 3 and queries:
        print(max(queries))

    if command == 4 and queries:
        print(min(queries))

print(", ".join([str(x) for x in queries[::-1]]))



# stacked_queries = []
# n = int(input())
#
# for i in range(n):
#     data = input()
#     if data.startswith("1"):
#         data_split = data.split()
#         number_to_add = int(data_split[1])
#         stacked_queries.append(number_to_add)
#
#     elif data == "2":
#         if stacked_queries:
#             stacked_queries.pop()
#     elif data == "3":
#         if stacked_queries:
#             print(max(stacked_queries))
#     elif data == "4":
#         if stacked_queries:
#             print(min(stacked_queries))
#
# stack_to_print = []
# while stacked_queries:
#     stack_to_print.append(str(stacked_queries.pop()))
# print(', '.join(stack_to_print))
#

# stack = []
# n = int(input())
# for i in range(n):
#     data = input()
#     data_split = data.split()
#     action = data_split[0]
#     if action == "1":
#         number = int(data_split[1])
#         stack.append(number)
#     elif action == "2":
#         if len(stack) > 0:
#             stack.pop()
#     elif action == "3":
#         if len(stack) > 0:
#             print(max(stack))
#     elif action == "4":
#         if len(stack) > 0:
#             print(min(stack))
#
# reversed_numbers = []
#
# for i in range(len(stack)):
#     if len(stack) > 0:
#         reversed_numbers.append(str(stack.pop()))
# print(", ".join(reversed_numbers))
