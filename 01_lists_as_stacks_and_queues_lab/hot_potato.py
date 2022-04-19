import sys
from io import StringIO

input1 = """Tracy Emily Daniel
2"""

sys.stdin = StringIO(input1)

from collections import deque

potato_players = deque(input().split())
n = int(input())

while potato_players:
    for _ in range(n - 1):
        potato_players.append(potato_players.popleft())
    out_player = potato_players.popleft()
    if potato_players:
        print(f'Removed {out_player}')
    else:
        print(f'Last is {out_player}')

