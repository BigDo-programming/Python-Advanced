import sys
from io import StringIO

input1 = '1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'

sys.stdin = StringIO(input1)

open_parentheses = []
text = input()
for i in range(len(text)):

    if text[i] == "(":
        open_parentheses.append(i)

    elif text[i] == ")":
        start_index = open_parentheses.pop()
        end_index = i
        print(text[start_index:end_index+1])



# expression = input()
# parentheses = []
#
# for index, ch in enumerate(expression):
#     if ch == '(':
#         parentheses.append(index)
#     elif ch == ')':
#         closing_index = index
#         opening_index = parentheses.pop()
#         print(expression[opening_index:closing_index+1])



