import sys
from io import StringIO

input1 = """348
20 54 30 16 7 9"""
input2 = """499
57 45 62 70 33 90 88 76 100 50"""
input3 = """"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

from collections import deque

quantity_of_food = int(input())
orders = deque(map(int, input().split()))
biggest_order = max(orders)

while orders:
    current_order = orders[0]
    if current_order > quantity_of_food:
        break

    else:
        quantity_of_food -= current_order
        orders.popleft()

print(biggest_order)
if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
else:
    print("Orders complete")
