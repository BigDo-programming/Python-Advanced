import sys
from io import StringIO
from pprint import pprint

input1 = """11, 6, 8, 1
3, 1, 9, 10, 5, 9, 1"""

input2 = """10, 9, 8, 7, 5
5, 10, 9, 8, 7"""

input3 = """12, -3, 14, 3, 2, 0
10, 15, 4, 6, 3, 1, 22, 1"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)
from collections import deque

pizza_orders = [int(x) for x in input().split(', ')]
pizza_orders = deque([x for x in pizza_orders if x > 0 and x <= 10])
employees = [int(x) for x in input().split(', ')]

pizzas = 0

while pizza_orders:
    if employees:
        pizza = pizza_orders.popleft()
        while pizza:

            last_employees = employees.pop()
            if pizza > last_employees:
                pizza -= last_employees
                pizzas += last_employees
                if employees:
                    continue
                else:
                    pizza_orders.append(pizza)
                    break # imam problem tuk!!!
            else:
                pizzas += pizza
                pizza -= last_employees
                break
    else:
        break

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas}")
    if employees:
        print(f'Employees: {", ".join([str(x) for x in employees])}')
else:
    print(f"Not all orders are completed.")
    if pizza_orders:
        print(f'Orders left: {", ".join([str(x) for x in reversed(pizza_orders)])}')