import sys
from io import StringIO

input1 = """1, 4, 5
4, 5, 6, 1, 3
2, 5, 10"""
sys.stdin = StringIO(input1)

numbers_list = [int(x) for x in input().split(", ")]
result = 1
for i in range(len(numbers_list)):
    number = numbers_list[i]

    if number <= 5:
        result *= number
    elif number > 5:
        result /= number
print(int(result))
