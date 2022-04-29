import sys
from io import StringIO

input1 = """1 2 -3 -4 65 -98 12 57 -84"""

sys.stdin = StringIO(input1)
my_numbers = [int(x) for x in input().split()]

negative = [x for x in my_numbers if x < 0]
positive = [x for x in my_numbers if x > 0]


negative_sum = sum(negative)
positive_sum = sum(positive)

print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
