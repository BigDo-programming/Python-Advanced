from cgitb import reset
import queue
import sys
from io import StringIO
from collections import deque

input1 = """George
Peter
William
Paid
Michael
Oscar
Olivia
Linda
End"""

sys.stdin = StringIO(input1)
# Queues Опашка (deque - from collections import deque) (първия елемент влязъл първи излиза - може да е от ляво на дясно и обратно)

queue = deque()
while True:
    command = input()

    if command == 'End':
        print(f'{len(queue)} people remaining.')
        break
    
    elif command == "Paid":
        while queue:
            print(queue.pop())

    else:
        queue.appendleft(command)

    