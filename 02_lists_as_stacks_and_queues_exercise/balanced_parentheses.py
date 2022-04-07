import sys
from io import StringIO

input1 = """{[()]}"""
input2 = """{[(])}"""
input3 = """"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

balanced = True
parentheses = input()
stack = []
for parent in parentheses:
    if parent in "{[(":
        stack.append(parent)

    elif parent in "}])":
        if len(stack) == 0:
            balanced = False
            break

        opening_paren = stack.pop()

        if f'{opening_paren}{parent}' not in ["[]", "{}", "()"]:
            balanced = False
            break

        # if parent == "]" and opening_paren == "[":
        #     continue
        # elif parent == "}" and opening_paren == "{":
        #     continue
        # elif parent == ")" and opening_paren == "(":
        #     continue


if balanced and len(stack) == 0:
    print("YES")
else:
    print("NO")
