import sys
from io import StringIO

input1 = """20, 24, -5, 17, 22, 60, 26
26, 60, 22, 17, 24, 10, 55"""

input2 = """-10, -2, -30, 10
-5"""

input3 = """2, 3, 3, 7, 2
2, 7, 3, 3, 2, 14, 6"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)
from collections import deque


chocolates = [int(x) for x in input().split(", ")]
milks = deque([int(x) for x in input().split(", ")])

milkshakes = 0
while chocolates and milks and milkshakes < 5:

    chocolate = chocolates.pop()
    milk = milks.popleft()

    if chocolate <= 0 and milk <= 0:
        continue
    if chocolate <= 0:
        milks.appendleft(milk)
        continue
    if milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        milks.append(milk)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")
if milks:
    print(f"Milk: {', '.join([str(x) for x in milks])}")
else:
    print("Milk: empty")


# from collections import deque
# chocolates = [int(x) for x in input().split(", ")]
# cups_of_milk = deque([int(x) for x in input().split(", ")])
# milkshakes = 0
#
# min_len = min(len(chocolates), len(cups_of_milk))
# for i in range(min_len):
#     chocolate = chocolates[-1]
#     milk = cups_of_milk[0]
#
#     if milkshakes == 5:
#         break
#
#     if chocolate <= 0:
#         chocolates.pop()
#         continue
#
#     if milk <= 0:
#         cups_of_milk.popleft()
#         continue
#
#     else:
#
#         if chocolate == milk:
#             milkshakes += 1
#             cups_of_milk.popleft()
#             chocolates.pop()
#
#         else:
#             chocolate -= 5
#
# if milkshakes == 5:
#     print("Great! You made all the chocolate milkshakes needed!")
# elif milkshakes < 5:
#     print("Not enough milkshakes.")
#
# if chocolates:
#     print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
# elif len(chocolates) <= 0:
#     print("Chocolate: empty")
#
# if cups_of_milk:
#     print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
# elif len(cups_of_milk) <= 0:
#     print("Milk: empty")