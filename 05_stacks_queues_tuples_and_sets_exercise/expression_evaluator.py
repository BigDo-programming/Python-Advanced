import sys
from io import StringIO

input1 = """6 3 - 2 1 * 5 /"""

input2 = """2 2 - 1 *"""

input3 = """10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

from collections import deque

arithmetic_expressions = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "/": lambda a, b: a // b,
    "*": lambda a, b: a * b,
}

expression = [int(x) if x not in arithmetic_expressions else str(x) for x in input().split()]
numbers = deque()

for i in expression:

    if i in arithmetic_expressions:
        result = numbers.popleft()
        while numbers:
            number = numbers.popleft()
            result = arithmetic_expressions[i](result, number)
        numbers.append(result)
    else:
        numbers.append(i)
print(numbers.popleft())
#
#
#
# arithmetic_expressions = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "/": lambda a, b: a // b,
#     "*": lambda a, b: a * b,
# }
#     # if ch == "-":
#     #     result -= number
#     # elif ch == "+":
#     #     result += number
#     # elif ch == "*":
#     #     result *= number
#     # elif ch == "/":
#     #     result /= number
#
#
# characters = input().split()
# numbers = deque()
#
# for ch in characters:
#     if ch in arithmetic_expressions:
#         result = numbers.popleft()
#         while numbers:
#             number = numbers.popleft()
#             result = arithmetic_expressions[ch](result, number)
#         numbers.append(result)
#
#     else:
#         numbers.append(int(ch))
#
# print(numbers.popleft())
