from ast import Expression
from cgitb import reset
import sys
from io import StringIO

input1 = '1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'

sys.stdin = StringIO(input1)

expression = input()
parentheses = []

for index, ch in enumerate(expression):
    if ch == '(':
        parentheses.append(index)
    elif ch == ')':
        closing_index = index
        opening_index = parentheses.pop()
        print(expression[opening_index:closing_index+1])


# Стек 'Stacks' (Последния елемент влязъл първи излиза) - е подмножество на листа е което се използва само apend() and pop()!!!
