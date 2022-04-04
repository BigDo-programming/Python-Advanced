# from cgitb import reset
# import sys
# from io import StringIO

# input1 = 'I Love Python'

# sys.stdin = StringIO(input1)


text = input()
string = []
for i in text:
    string.append(i)


result = ''
while len(string) > 0:
    result += string.pop()

print(result)

# Стек 'Stacks' (Последния елемент влязъл първи излиза) - е подмножество на листа е което се използва само apend() and pop()!!!