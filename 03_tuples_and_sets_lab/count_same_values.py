
import sys
from io import StringIO

input1 = "-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3"

sys.stdin = StringIO(input1)

same_values = {}
values = [float(x) for x in input().split()]
for i in values:
    if i not in same_values:
        same_values[i] = 1
    else:
        same_values[i] += 1


for key,value in same_values.items():
    print(f"{key} - {value} times")































#
#
# numbers_count = {}
# numbers = [float(x) for x in input().split()]
#
# for number in numbers:
#     if number not in numbers_count:
#         numbers_count[number] = 0
#     numbers_count[number] += 1
#
# for number, count in numbers_count.items():
#     print(f"{number} - {count} times")