import sys
from io import StringIO

input1 = """10 -5 20 15 -30 10
40 60 10 4 10 0"""

input2 = """30 5 15 60 0 30
-15 10 5 -15 25"""

input3 = """30 10
15 10 5 0 10"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)
from collections import deque

materials_for_crafting = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

crafted_presents = {}

while materials_for_crafting and magic_level:
    box = materials_for_crafting.pop()
    magic_value = magic_level.popleft()
    result = box * magic_value
    if box == 0 and magic_value == 0:
        continue
    if box == 0:
        magic_level.appendleft(magic_value)
        continue

    if magic_value == 0:
        materials_for_crafting.append(box)
        continue

    if result < 0:
        materials_for_crafting.append(box + magic_value)

    elif result in presents:
        present = presents[result]

        if present in crafted_presents:
            crafted_presents[present] += 1
        else:
            crafted_presents[present] = 1
    else:
        materials_for_crafting.append(box + 15)
is_done = ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or \
          ("Bicycle" in crafted_presents and "Teddy bear" in crafted_presents)

if is_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_for_crafting:
    print(f"Materials left: {', '.join([str(x) for x in materials_for_crafting])}")
if magic_level:
    print(f"Materials left: {', '.join([str(x) for x in magic_level])}")

for toy_name, amount in sorted(crafted_presents.items()):
    print(f"{toy_name}: {amount}")

# ToDo има грешка