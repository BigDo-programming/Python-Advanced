import sys
from io import StringIO

input1 = """Odd
1 3 5 34 7 9 12 11 13 10"""

sys.stdin = StringIO(input1)

command = input()
my_numbers = [int(x) for x in input().split()]

parity = 0 if command == "Even" else 1
result = sum([x for x in my_numbers if x % 2 == parity]) * len(my_numbers)

print(result)

# command = input()
# my_numbers = [int(x) for x in input().split()]
# odd = sum([x for x in my_numbers if x % 2 == 0])
# even = sum([x for x in my_numbers if x % 2 == 1])
#
# # for i in my_numbers:
# #     if i % 2 == 0:
# #         even.append(i)
# #     else:
# #         odd.append(i)
# if command == "Odd":
#     print(odd * len(my_numbers))
# else:
#     print(even * len(my_numbers))
