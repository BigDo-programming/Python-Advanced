import sys
from io import StringIO

input1 = """1 2 3 4 5
1 2 3
3
Add First 5 6
Remove Second 8 9 11
Check Subset
"""

input2 = """5 4 2 9 9 5 4
1 1 1 5 6 5
4
Add First 5 6 9 3
Add Second 1 2 3 3 3
Check Subset
Remove Second 1 2 3 4 5"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

numbers_1 = set({int(x) for x in input().split()})
numbers_2 = set({int(x) for x in input().split()})

n = int(input())
for _ in range(n):
    data = input().split()
    command = data[0] + " " + data[1]
    if command == "Add First":
        numbers = set([int(x) for x in data[2:]])
        numbers_1.update(numbers)

    elif command == "Add Second":
        numbers = set([int(x) for x in data[2:]])
        numbers_2.update(numbers)

    elif command == "Remove First":
        numbers = set([int(x) for x in data[2:]])
        numbers_1.difference_update(numbers)

    elif command == "Remove Second":
        numbers = set([int(x) for x in data[2:]])
        numbers_2.difference_update(numbers)

    elif command == "Check Subset":
        print(numbers_1.issubset(numbers_2) or numbers_2.issubset(numbers_1))

        # if numbers_1.issubset(numbers_2) or numbers_2.issubset(numbers_1):
        #     print("True")
        # else:
        #     print("False")

print(', '.join([str(x) for x in sorted(numbers_1)]))
print(', '.join([str(x) for x in sorted(numbers_2)]))
