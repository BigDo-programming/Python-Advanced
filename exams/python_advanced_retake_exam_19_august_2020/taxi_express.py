import sys
from io import StringIO


input1 = """4, 6, 8, 5, 1
1, 9, 15, 10, 6"""

input2 = """10, 5, 8, 9
2, 4, 5, 8"""

input3 = """2, 8, 4, 3, 11, 7
10, 15, 4, 6, 3, 10, 2, 1"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]
total_time = 0
while customers:
    if len(taxis) == 0:
        break
    customer = customers.popleft()

    taxi = taxis.pop()
    if taxi >= customer:
        total_time += customer
    else:
        customers.appendleft(customer)

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
