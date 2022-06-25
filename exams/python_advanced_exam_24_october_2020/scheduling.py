import sys

from io import StringIO

input1 = """3, 1, 10, 1, 2
0"""

input2 = """4, 10, 10, 6, 2, 99
2"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)


from collections import deque

task = [int(x) for x in input().split(", ")]
searched_index = int(input())

jobs = deque(sorted([(task[x], x) for x in range(len(task))]))
work = 0
while jobs:

    value, index = jobs.popleft()
    work += value
    if searched_index == index:
        break

print(work)


# def get_keys_from_value(d, val):
#     key = None
#     for key, value in d.items():
#         if value == val:
#             break
#
#     return key
#
#
# jobs = [int(x) for x in input().split(", ")]
# index = int(input())
# number = jobs[index]
# job = {}
# for i in range(len(jobs)):
#     job[i] = jobs[i]
#
# work = 0
# while job:
#     minimum = min(job.values())
#     key = get_keys_from_value(job, minimum)
#     work += minimum
#     if index == key:
#         break
#
#     del job[key]
#
# print(work)


# from collections import deque
#
# task = [int(x) for x in input().split(", ")]
# searched_index = int(input())
#
# jobs = deque(sorted([(task[x], x) for x in range(len(task))]))
# work = 0
# for value, index in jobs:
#     work += value
#     if searched_index == index:
#         break
#
# print(work)
