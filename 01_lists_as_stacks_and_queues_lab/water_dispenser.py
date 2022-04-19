import sys
from io import StringIO

input1 = """2
Peter
Amy
Start
2
refill 1
1
End"""
input2 = """10
Peter
George
Amy
Alice
Start
2
3
3
3
End"""
# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

from collections import deque

queue = deque()
quantity_of_water = int(input())

name = input()
while not name == "Start":
    queue.append(name)
    name = input()

command = input()
while not command == 'End':

    if command.startswith("refill"):
        command_split = command.split()
        add_water = int(command_split[1])
        quantity_of_water += add_water
    else:
        wanted_water = int(command)
        if wanted_water <= quantity_of_water:
            quantity_of_water -= wanted_water
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")

    command = input()

print(f"{quantity_of_water} liters left")











# people_queue = deque()
# water_quantity = int(input())
# while True:
#     command = input()
#     if command == 'Start':
#         break
#     people_queue.appendleft(command)
#
# while True:
#
#     command = input()
#     if command == 'End':
#         break
#
#     elif command.startswith('refill'):
#         params = command.split()
#         liters_to_add = int(params[1])
#         water_quantity += liters_to_add
#
#     else:
#         name = people_queue.pop()
#         water_wanted = int(command)
#         if water_wanted <= water_quantity:
#             print(f"{name} got water")
#             water_quantity -= water_wanted
#         else:
#             print(f'{name} must wait')
#
# print(f'{water_quantity} liters left')