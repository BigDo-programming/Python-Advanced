import sys
from io import StringIO

input1 = """4 6"""
input2 = """3 2"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

n, m = [int(x) for x in input().split()]
for i in range(n):
    for j in range(m):
        print(chr(97 + i), chr(97 + j + i), chr(97 + i), sep="", end=" ")
    print()

# n, m = [int(x) for x in input().split()]
# for r in range(n):
#     for c in range(m):
#         print(f"{chr(97 + r)}{chr(97 + r + c)}{chr(97 + r)}", end=" ")
#     print()


# n, m = [int(x) for x in input().split()]
# for r in range(n):
#     for c in range(m):
#         print(f"{chr(97 + r)}{chr(97 + r + c)}{chr(97 + r)}", end=" ")
#     print()
