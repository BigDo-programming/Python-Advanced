import sys
from io import StringIO

input1 = """4
Pesho
Stefan
Stamat
Gosho"""

input2 = """6
Preslav
Gosho
Ivan
Stamat
Pesho
Stefan"""

sys.stdin = StringIO(input1)

# sys.stdin = StringIO(input2)

n = int(input())
even_set = set()
odd_set = set()
for i in range(1, n + 1):
    name = input()

    name_sum = 0
    for ch in name:
        name_sum += ord(ch)
    ch_number = name_sum // i
    if ch_number % 2 == 0:
        even_set.add(ch_number)
    else:
        odd_set.add(ch_number)

if sum(even_set) == sum(odd_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(even_set) < sum(odd_set):
    print(*odd_set.difference(even_set), sep=", ")
elif sum(even_set) > sum(odd_set):
    print(*odd_set.symmetric_difference(even_set), sep=", ")

# odd_set = set()
# even_set = set()
# n = int(input())
#
# for i in range(1, n + 1):
#     name_sum = 0
#     name = input()
#     for ch in name:
#         name_sum += ord(ch)
#     if name_sum // i % 2 == 0:
#         even_set.add(name_sum // i)
#     else:
#         odd_set.add(name_sum // i)
#
# if sum(odd_set) == sum(even_set):
#
#     print(", ".join([str(x) for x in odd_set.union(even_set)]))
# elif sum(odd_set) > sum(even_set):
#
#     print(", ".join([str(x) for x in odd_set.difference(even_set)]))
# else:
#     print(", ".join([str(x) for x in odd_set.symmetric_difference(even_set)]))


# n = int(input())
# odd_set = set()
# even_set = set()
# for i in range(1, n + 1):
#     name = input()
#     name_sum = sum([ord(x) for x in name]) // i
#
#     if name_sum % 2 == 0:
#         even_set.add(name_sum)
#     else:
#         odd_set.add(name_sum)
#
# if sum(odd_set) == sum(even_set):
#     print(', '.join([str(x) for x in odd_set.union(even_set)]))
# elif sum(odd_set) > sum(even_set):
#     print(', '.join([str(x) for x in odd_set.difference(even_set)]))
# elif sum(odd_set) < sum(even_set):
#     print(', '.join([str(x) for x in even_set.symmetric_difference(odd_set)]))
