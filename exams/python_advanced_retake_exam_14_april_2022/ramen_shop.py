import sys
from io import StringIO

input1 = """14, 25, 37, 43, 19
58, 23, 37"""

input2 = """30, 13, 45
70, 25, 55, 15"""

input3 = """30, 25
20, 35"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)
from collections import deque

bowls_ramen = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while bowls_ramen or customers:

    if not bowls_ramen:
        break
    if not customers:
        break

    ramen = bowls_ramen.pop()
    customer = customers.popleft()
    if ramen > customer:
        ramen -= customer
        bowls_ramen.append(ramen)
    elif customer > ramen:
        customer -= ramen
        customers.appendleft(customer)
    else:
        continue

if not customers:
    print("Great job! You served all the customers.")
    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_ramen])}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")

