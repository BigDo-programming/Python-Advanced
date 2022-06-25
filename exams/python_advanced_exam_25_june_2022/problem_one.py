import sys
from io import StringIO

input1 = """20, 13, -7, 7
10, 5, 20, 15, 7, 9"""

input2 = """2, 4, 7, 8, 0
5, 6, 2"""

input3 = """12, 23
28, 40"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


from collections import deque

box = 0
eggs = deque([int(x) for x in input().split(', ')])
papers = [int(x) for x in input().split(', ')]

while eggs or papers:
    if not eggs:
        break

    if not papers:
        break
    egg = eggs.popleft()
    if egg <= 0:
        continue
    if egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue
    paper = papers.pop()
    result = egg + paper
    if not result <= 50:
        continue
    box += 1

if box:
    print(f"Great! You filled {box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f'Eggs left: {", ".join([str(x) for x in eggs])}')
if papers:
    print(f'Pieces of paper left: {", ".join([str(x) for x in papers])}')

