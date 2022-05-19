import sys
from io import StringIO

input1 = """{[()]}"""
input2 = """{[(])}"""
input3 = """)()"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

parentheses_open = []
parentheses = list(input())
is_balanced = True
for i in parentheses:

    if i in "{[(":
        parentheses_open.append(i)

    elif parentheses_open:
        open_parentheses = parentheses_open.pop()

        if not open_parentheses + i in "{},[],()":
            is_balanced = False
            break
    else:
        is_balanced = False
        break


if not parentheses_open and is_balanced:
    print("YES")
else:
    print("NO")

# open_parentheses = []
# is_balanced = False
# parentheses = list(input())
#
# for i in parentheses:
#     if i in "{" "(" '[':
#         open_parentheses.append(i)
#
#     elif len(open_parentheses) > 0:
#         if open_parentheses[-1] + i in "{}""[]""()":
#             open_parentheses.pop()
#             is_balanced = True
#
#         else:
#             is_balanced = False
#             break
#
#     else:
#         is_balanced = False
#         break
#
# if is_balanced:
#     print("YES")
# else:
#     print("NO")

# balanced = True
# parentheses = input()
# stack = []
# for parent in parentheses:
#     if parent in "{[(":
#         stack.append(parent)
#
#     elif parent in "}])":
#         if len(stack) == 0:
#             balanced = False
#             break
#
#         opening_paren = stack.pop()
#
#         if f'{opening_paren}{parent}' not in ["[]", "{}", "()"]:
#             balanced = False
#             break
#
# if balanced and len(stack) == 0:
#     print("YES")
# else:
#     print("NO")
