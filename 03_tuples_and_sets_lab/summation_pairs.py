import sys
from io import StringIO

input1 = """1 5 4 2 2 3 1 3 2
4"""

input2 = """11 8 5 6 9 2 9 7 3 4
11 """
sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

from collections import deque


unique_pairs = set()

iterations = 0
numbers = deque([int(x) for x in input().split()])
target_number = int(input())
number = 0
for i in range(len(numbers)):
    number = numbers.popleft()

    for j in range(len(numbers)):
        iterations += 1
        if number + numbers[j] == target_number:

            print(f"{number} + {numbers[j]} = {target_number}")
            unique_pairs.add(f"({number}, {numbers[j]})")

numbers.append(number)
print(f"Iterations done: {iterations}")
for i in unique_pairs:
    print(i)


















#
# total_number_of_iterations = 0
# sequence_of_numbers = set()
# sequence = deque([int(x) for x in input().split()])
# search_number = int(input())
# number = 0

# for _ in range(len(sequence)):
#     number = sequence.popleft()
#
#     for i in range(len(sequence)):
#         total_number_of_iterations += 1
#         if sequence[i] + number == search_number:
#             sequence_of_numbers.add((number, sequence[i]))
#             print(f"{number} + {sequence[i]} = {search_number}")
#
# sequence.append(number)
# print(f"Iterations done: {total_number_of_iterations}")
# [print(x) for x in sequence_of_numbers]

