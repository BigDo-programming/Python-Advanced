import sys
from io import StringIO

input1 = """20 62 99 35 0 150
120 60 10 1 70 10
+ - + + / * - - /"""

input2 = """30
15 9 5 150 8
* + + * -"""

input3 = """"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)
from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
honey_making_process = deque(input().split())

total_honey = 0
while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= current_bee:
        sing = honey_making_process.popleft()
        if sing == "+":
            total_honey += abs(current_bee + current_nectar)
        elif sing == "-":
            total_honey += abs(current_bee - current_nectar)
        elif sing == "/":
            if current_nectar > 0:
                total_honey += abs(current_bee / current_nectar)
        elif sing == "*":
            total_honey += abs(current_bee * current_nectar)

    else:
        working_bees.appendleft(current_bee)

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")