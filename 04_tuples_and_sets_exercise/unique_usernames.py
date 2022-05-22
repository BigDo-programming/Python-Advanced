import sys
from io import StringIO

input1 = """6
George
George
George
Peter
George
NiceGuy1234"""

sys.stdin = StringIO(input1)

valid_username = set()
for i in range(int(input())):
    valid_username.add(input())

[print(x) for x in valid_username]


# n = int(input())
# names = set()
# for i in range(n):
#     names.add(input())
# [print(x) for x in names]



# unique_usernames = set()
# n = int(input())
# for _ in range(n):
#     name = input()
#     unique_usernames.add(name)
# [print(x) for x in unique_usernames]
