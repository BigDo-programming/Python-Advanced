import sys
from io import StringIO

input1 = """5
5, 15, 25, 35"""

input2 = """30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

from collections import deque

bombs = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs",
}
crafted_bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0,
}
is_done = False
bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

while True:
    if len(bomb_effects) == 0:
        break
    if len(bomb_casings) == 0:
        break

    if crafted_bombs["Datura Bombs"] >= 3 and crafted_bombs["Cherry Bombs"] >= 3 and crafted_bombs[
        "Smoke Decoy Bombs"] >= 3:
        is_done = True
        break

    creating_bomb = int(bomb_effects[0] + bomb_casings[-1])
    if creating_bomb in bombs:
        crafted_bombs[bombs[creating_bomb]] += 1
        bomb_effects.popleft()
        bomb_casings.pop()


    else:
        bomb_casings[-1] -= 5

if is_done:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")
for key, value in sorted(crafted_bombs.items()):
    print(f"{key}: {value}")
