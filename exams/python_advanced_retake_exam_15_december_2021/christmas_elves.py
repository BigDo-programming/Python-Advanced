import sys
from io import StringIO

input1 = """10 16 13 25
12 11 8"""

input2 = """10 14 22 4 5
11 16 17 11 1 8"""

input3 = """5 6 7
2 1 5 7 5 3"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

from collections import deque

elfs_energy = deque([int(x) for x in input().split()])
materials_in_box = [int(x) for x in input().split()]

total_elves_energy_used = 0
total_successfully_made_toys = 0
turn = 0

while elfs_energy or materials_in_box:
    if not elfs_energy:
        break

    if not materials_in_box:
        break

    elf = elfs_energy.popleft()
    if elf < 5:
        continue
    turn += 1
    box = materials_in_box.pop()

    if turn % 3 == 0:
        if not turn % 5 == 0:
            if elf >= box * 2:
                elf -= box * 2
                total_successfully_made_toys += 2
                total_elves_energy_used += box * 2
                elf += 1
                elfs_energy.append(elf)
            else:
                materials_in_box.append(box)
                elfs_energy.append(elf * 2)

        if turn % 5 == 0:
            if elf >= box * 2:
                elf -= box * 2
                total_elves_energy_used += box * 2
                elfs_energy.append(elf)

            else:
                materials_in_box.append(box)
                elfs_energy.append(elf * 2)

    elif turn % 5 == 0:
        if elf >= box:
            elf -= box
            total_elves_energy_used += box
            elfs_energy.append(elf)
        else:
            materials_in_box.append(box)
            elfs_energy.append(elf * 2)

    elif elf >= box:
        elf -= box
        total_successfully_made_toys += 1
        total_elves_energy_used += box
        elfs_energy.append(elf + 1)
    else:
        materials_in_box.append(box)
        elfs_energy.append(elf * 2)

print(f"Toys: {total_successfully_made_toys}")
print(f"Energy: {total_elves_energy_used}")
if elfs_energy:
    print(f"Elves left: {', '.join([str(x) for x in elfs_energy])}")
if materials_in_box:
    print(f"Boxes left: {', '.join([str(x) for x in materials_in_box])}")
