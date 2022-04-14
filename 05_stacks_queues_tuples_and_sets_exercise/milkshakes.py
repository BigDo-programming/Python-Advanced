import sys
from io import StringIO

input1 = """20, 24, -5, 17, 22, 60, 26
26, 60, 22, 17, 24, 10, 55"""

input2 = """"""

input3 = """"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)
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
