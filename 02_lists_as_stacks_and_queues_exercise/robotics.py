import sys
from io import StringIO

input1 = """ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End"""

input2 = """ROB-8
7:59:59
detail
glass
wood
sock
End"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
from math import floor
from collections import deque


def robots_and_time():
    robots_time = deque()
    bots = input().split(";")
    for i in bots:
        robot_, time_ = i.split("-")
        robots_time.append([robot_, int(time_), 0])
    return robots_time


# processing_time


robots = robots_and_time()
product_line = deque()
time_start = input()  # da go oprawq
time_start = 0

command = input()
while not command == "End":
    product_line.append(command)
    command = input()

working = {}
while product_line:
    product = product_line.popleft()
    for robot, time, work in robots:
        if work == 0:
            working[time_start + 1] = [robot, product, time + time_start]
            robots[0][2] = 1
            time_start += 1
            robots.rotate(-1)

        elif time_start == robots[-1][1]:
            robots[0][2] = 0
            product_line.appendleft(product)

        else:
            time_start += 1
            product_line.appendleft(product)

print(working)










# ToDo да я довърша
# class Robot:
#     def __init__(self, name, processing_time):
#         self.processing_time = processing_time
#         self.name = name
#         self.busy_until = 0
#
#
# def get_seconds_for_time(time):
#     hours, minutes, seconds = [int(x) for x in time.split(":")]
#     return hours * 60 * 60 + minutes * 60 + seconds
#
#
# def get_time_from_seconds(seconds):
#     seconds %= (24 * 60 * 60)
#     hours = seconds // (60 * 60)
#     minutes = floor((seconds / 60) % 60)
#     # seconds = seconds - (hours * 60 * 60) - (minutes * 60)
#     seconds = seconds % 60
#     return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#
#
# robots = []
# robots_input = input().split(";")
# for robot_input in robots_input:
#     robot_name, processing_time = robot_input.split("-")
#     robots.append(Robot(robot_name, int(processing_time)))
#
# time_in_seconds = get_seconds_for_time(input())
# items = deque()
#
# while True:
#     item = input()
#     if item == "End":
#         break
#     items.append(item)
#
# while items:
#     current_item = items.popleft()
#     time_in_seconds += 1
#     found_robot = False
#
#     for robot in robots:
#         if time_in_seconds >= robot.busy_until:
#             robot.busy_until = time_in_seconds + robot.processing_time
#             found_robot = True
#             print(f"{robot.name} - {current_item} [{get_time_from_seconds(time_in_seconds)}]")
#             break
#     if not found_robot:
#         items.append(current_item)
