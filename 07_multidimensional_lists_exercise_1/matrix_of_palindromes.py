import sys
from io import StringIO

input1 = """4 6"""

sys.stdin = StringIO(input1)

n, m = [int(x) for x in input().split()]
for r in range(n):
    for c in range(m):
        print(f"{chr(97 + r)}{chr(97 + r + c)}{chr(97 + r)}", end=" ")
    print()



# n, m = [int(x) for x in input().split()]
# for r in range(n):
#     for c in range(m):
#         print(f"{chr(97 + r)}{chr(97 + r + c)}{chr(97 + r)}", end=" ")
#     print()
