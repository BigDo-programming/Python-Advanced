# from cgitb import reset
# import sys
# from io import StringIO

# input1 = "-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3"

# sys.stdin = StringIO(input1)

numbers_count = {}
numbers = [float(x) for x in input().split()]

for number in numbers:
    if number not in numbers_count:
        numbers_count[number] = 0
    numbers_count[number] += 1

for number, count in numbers_count.items():
    print(f"{number} - {count} times")