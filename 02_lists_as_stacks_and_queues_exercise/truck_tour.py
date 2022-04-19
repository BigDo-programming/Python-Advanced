import sys
from io import StringIO

input1 = """3
1 5
10 3
3 4"""
input2 = """5
22 5
14 10
52 7
21 12
36 9"""
input3 = """"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


from collections import deque

petrol_pump = []
n = int(input())
for i in range(n):
    data = [int(x) for x in input().split()]
    petrol_pump.append(data)


for i,j in petrol_pump:
    print(i,j)














# queue = deque()
# n = int(input())
#
#
# for i in range(n):
#     pump = [int(x) for x in input().split()]
#     queue.append(pump)
#
# for index in range(n):
#     car_fuel = 0
#     completed = True
#     for petrol, distance in queue:
#
#         car_fuel += petrol
#         if distance > car_fuel:
#             completed = False
#             break
#         car_fuel -= distance
#     if completed:
#
#         break
#
#     queue.append(queue.popleft())
#
# print(index)