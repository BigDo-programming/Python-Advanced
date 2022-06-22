import sys

from io import StringIO

input1 = """4 5 7 3 6 9 12
12 9 6 1"""

input2 = """3 0 3 6 9 0 12
12 9 6 1 2 3 15 13 4"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)


from collections import deque

match = 0
males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

while males or females:
    if not males:
        break
    if not females:
        break

    male = males.pop()
    female = females.popleft()

    if male <= 0:
        females.appendleft(female)
        continue

    if female <= 0:
        males.append(male)
        continue

    if male % 25 == 0:
        females.appendleft(female)
        males.pop()
        continue

    if female % 25 == 0:
        males.append(male)
        females.popleft()
        continue

    if female == male:
        match += 1
    else:
        males.append(male - 2)

print(f"Matches: {match}")
if not males:
    print("Males left: none")
else:
    print(f"Males left: {', '.join([str(x) for x in males[::-1]])}")
if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join([str(x) for x in females])}")

# males = [int(x) for x in input().split()]
# females = deque([int(x) for x in input().split()])
# matches = 0
# while males and females:
#     male = males[-1]
#     female = females[0]
#     if male <= 0:
#         males.pop()
#         continue
#     if female <= 0:
#         females.popleft()
#         continue
#     if male % 25 == 0:
#         males.pop()
#         males.pop()
#         continue
#     if female % 25 == 0:
#         females.popleft()
#         females.popleft()
#         continue
#     if male == female:
#         matches += 1
#         males.pop()
#         females.popleft()
#     elif not male == female:
#         females.popleft()
#         males[-1] -= 2
#
# print(f"Matches: {matches}")
# if not males:
#     print("Males left: none")
# else:
#     print(f"Males left: {', '.join([str(x) for x in males[::-1]])}")
# if not females:
#     print("Females left: none")
# else:
#     print(f"Females left: {', '.join([str(x) for x in females])}")