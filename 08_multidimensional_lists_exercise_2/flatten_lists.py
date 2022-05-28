import sys
from io import StringIO

input1 = """1 2 3 |4 5 6 |  7  88"""
input2 = """1| 4 5 6 7  |  8 9"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

# import re
# text = input().split("|")
# new_text = " ".join([x for x in list(reversed(text))])
# match = re.findall(r"\d+",new_text)
#
# print(*match)


result = []
text = input().split("|")
for i in range(len(text) -1, -1,-1):
    new_text = text[i].strip().split()
    result.extend(new_text)

print(*result)





























# result = []
# data = input().split("|")
# while data:
#     sublist = data.pop().split()
#     for el in sublist:
#         result.append(el)
#
# print(*result)


# sublist = input().split("|")
# result = []
# for index in range(len(sublist) - 1, -1, -1):
#     elements = sublist[index].split()
#     print(*elements, end=" ")
