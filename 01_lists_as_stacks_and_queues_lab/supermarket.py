import sys
from io import StringIO

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

from collections import deque

queue = deque()
command = input()
while not command == "End":
    if command == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)

    command = input()
print(f"{len(queue)} people remaining.")

# queue = deque()
# while True:
#     command = input()
#
#     if command == 'End':
#         print(f'{len(queue)} people remaining.')
#         break
#
#     elif command == "Paid":
#         while queue:
#             print(queue.pop())
#
#     else:
#         queue.appendleft(command)
