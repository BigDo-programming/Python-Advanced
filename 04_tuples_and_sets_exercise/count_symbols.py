import sys
from io import StringIO

input1 = """SoftUni rocks"""

input2 = """Why do you like Python?"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

count_symbols = {}
text = input()
for i in text:
    if i not in count_symbols:
        count_symbols[i] = 0

    count_symbols[i] += 1

for key, value in sorted(count_symbols.items()):
    print(f"{key}: {value} time/s")

#
# count_symbols = {}
# text = input()
#
# for i in text:
#     if i not in count_symbols:
#         count_symbols[i] = 0
#
#     count_symbols[i] += 1
#
# for key,value in sorted(count_symbols.items()):
#     print(f"{key}: {value} time/s")
