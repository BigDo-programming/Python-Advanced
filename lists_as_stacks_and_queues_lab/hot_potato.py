from cgitb import reset
import queue
import sys
from io import StringIO
from collections import deque

input1 = """George Peter Michael William Thomas
10"""

sys.stdin = StringIO(input1)
potatos = input().split()

potatos_queue = deque(potatos)
step = int(input())

while potatos_queue:
    for _ in range(step - 1):
        potatos_queue.append(potatos_queue.popleft())
    potatos_to_remove = potatos_queue.popleft()

    if potatos_queue:
        print(f'Removed {potatos_to_remove}')
    else:
        print(f'Last is {potatos_to_remove}')
