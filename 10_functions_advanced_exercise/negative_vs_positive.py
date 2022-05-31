import sys
from io import StringIO

input1 = """1 2 -3 -4 65 -98 12 57 -84"""

sys.stdin = StringIO(input1)


def stronger_positive_or_negative(*args):
    positive = [x for x in args if x > 0]
    negative = [x for x in args if x <= 0]
    print(sum(negative))
    print(sum(positive))
    # positive_or_negative = "positives" if sum(positive) > sum(negative) else "negatives"
    if abs(sum(negative)) > sum(positive):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")



nums = [int(x) for x in input().split()]
stronger_positive_or_negative(*nums)






# my_numbers = [int(x) for x in input().split()]
#
# negative = [x for x in my_numbers if x < 0]
# positive = [x for x in my_numbers if x > 0]
#
#
# negative_sum = sum(negative)
# positive_sum = sum(positive)
#
# print(negative_sum)
# print(positive_sum)
# if abs(negative_sum) > positive_sum:
#     print("The negatives are stronger than the positives")
# else:
#     print("The positives are stronger than the negatives")
