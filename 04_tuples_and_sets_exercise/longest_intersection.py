import sys
from io import StringIO

input1 = """5
0,10-2,5
3,8-1,7
1,8-2,4
4,7-2,5
1,10-2,11"""

input2 = """3
0,3-1,2
2,10-3,5
6,15-3,10"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

longest_intersection = {}
set1 = set()
set2 = set()
n = int(input())
for i in range(n):

    first_one, second_one = input().split("-")
    first_start, first_end = [int(x) for x in first_one.split(",")]
    second_start, second_end = [int(x) for x in second_one.split(",")]

    for f in range(first_start, first_end + 1):
        set1.add(f)

    for s in range(second_start, second_end + 1):
        set2.add(s)
    list_intersection = list(set1.intersection(set2))

    longest_intersection[len(list_intersection)] = list_intersection
    set1.clear()
    set2.clear()

print(
    f"Longest intersection is [{', '.join([str(x) for x in longest_intersection[max(longest_intersection)]])}] with length {max(longest_intersection)}")



# def intersection_set(dict, first_part, second_part):
#     set1 = set()
#     set2 = set()
#
#     for i in range(first_part[0], first_part[1] + 1):
#         set1.add(i)
#     for j in range(second_part[0], second_part[1] + 1):
#         set2.add(j)
#
#     dict[len(set1.intersection(set2))] = set1.intersection(set2)
#
#     return max(dict.items())

# intersection = {}
# n = int(input())
# for _ in range(n):
#     sets = input().split("-")
#     first = [int(x) for x in sets[0].split(",")]
#     second = [int(x) for x in sets[1].split(",")]
#     intersection_set(intersection, first, second)

# longest_intersection = max(intersection)

# print(f"Longest intersection is {[x for x in intersection[longest_intersection]]} with length {longest_intersection}")

# n = int(input())
# longest_intersection = set()
# for _ in range(n):
#     first_str, second_str = [x.split(",") for x in input().split("-")]
#     first_start, first_end = [int(x) for x in first_str]
#     second_start, second_end = [int(x) for x in second_str]
#
#     first_range = set(range(first_start, first_end + 1))
#     second_range = set(range(second_start, second_end + 1))
#
#     current_intersection = first_range.intersection(second_range)
#
#     if len(current_intersection) > len(longest_intersection):
#         longest_intersection = current_intersection
#
# print(f"Longest intersection is [{', '.join([str(x) for x in longest_intersection])}] with length {len(longest_intersection)}")
