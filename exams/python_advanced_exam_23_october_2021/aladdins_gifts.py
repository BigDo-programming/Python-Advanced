import sys
from io import StringIO

input1 = """105 20 30 25
120 60 11 400 10 1"""

input2 = """30 5 21 6 0 91
15 9 5 15 8"""

input3 = """200
5 15 32 20 10 5"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from collections import deque


def wedding_presents(value):
    if 100 <= value <= 199:
        return "Gemstone"
    elif 200 <= value <= 299:
        return "Porcelain Sculpture"
    elif 300 <= value <= 399:
        return "Gold"
    elif 400 <= value <= 499:
        return "Diamond Jewellery"
    return False


presents = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}

materials = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])

while magics or materials:
    if not materials:
        break
    if not magics:
        break
    material = materials.pop()
    magic = magics.popleft()
    mix = material + magic

    if mix < 100 and mix % 2 == 0:
        mix = (material * 2) + (magic * 3)

    elif mix < 100 and mix % 1 == 0:
        mix *= 2

    elif mix > 499:
        mix /= 2

    result = wedding_presents(mix)
    if result:
        presents[result] += 1

    else:
        continue

if presents["Gemstone"] > 0 and presents["Porcelain Sculpture"] > 0 or presents["Gold"] > 0 and presents[
    "Diamond Jewellery"] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magics:
    print(f"Magic left: {', '.join([str(x) for x in magics])}")
for key, value in sorted(presents.items()):
    if value > 0:
        print(f"{key}: {value}")
