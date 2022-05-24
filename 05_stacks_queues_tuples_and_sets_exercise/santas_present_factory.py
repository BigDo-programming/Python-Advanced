import sys
from io import StringIO

input1 = """10 -5 20 15 -30 10
40 60 10 4 10 0"""

input2 = """30 5 15 60 0 30
-15 10 5 -15 25"""

input3 = """30 0
0 10 5 0 10"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)
from collections import deque

santa_present_factory = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

present_factory = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0,
}

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

while materials and magic_level:

    material = materials.pop()
    magic = magic_level.popleft()
    value = material * magic

    if material == 0 and magic == 0:
        continue

    if material == 0:
        magic_level.appendleft(magic)
        continue

    if magic == 0:
        materials.append(material)
        continue

    if value < 0:
        materials.append(material + magic)

    elif value in santa_present_factory:
        present_factory[santa_present_factory[value]] += 1

    else:
        materials.append(material + 15)

if present_factory["Teddy bear"] >= 1 and present_factory["Bicycle"] >= 1 or present_factory["Doll"] >= 1 and \
        present_factory["Wooden train"] >= 1:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials[::-1]])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

for key, value in sorted(present_factory.items()):
    if value > 0:
        print(f"{key}: {value}")

# present = {
#     150: "Doll",
#     250: "Wooden train",
#     300: "Teddy bear",
#     400: "Bicycle",
# }
# santa_present = {
#     "Doll": 0,
#     "Wooden train": 0,
#     "Teddy bear": 0,
#     "Bicycle": 0,
# }
# boxes = [int(x) for x in input().split()]
# magic = deque([int(x) for x in input().split()])
#
# while boxes and magic:
#     current_box = boxes.pop()
#     current_magic = magic.popleft()
#     result = current_magic * current_box
#
#     if current_box == 0 and current_magic == 0:
#         continue
#
#     if current_box == 0:
#         magic.appendleft(current_magic)
#         continue
#
#     if current_magic == 0:
#         boxes.append(current_box)
#         continue
#
#     if result < 0:
#         boxes.append(current_magic + current_box)
#
#     elif result in present:
#         new_present = present[result]
#
#         if new_present in santa_present:
#             santa_present[new_present] += 1
#         else:
#             santa_present[new_present] = 1
#
#     else:
#         boxes.append(current_box + 15)
#
# if (santa_present["Doll"] > 0 and santa_present["Wooden train"] > 0) or santa_present["Teddy bear"] > 0 and \
#         santa_present["Bicycle"] > 0:
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
# if boxes:
#     print(f"Materials left: {', '.join([str(x) for x in boxes[::-1]])}")
# if magic:
#     print(f"Magic left: {', '.join([str(x) for x in magic])}")
# for key, value in sorted(santa_present.items()):
#     if value > 0:
#         print(f"{key}: {value}")

#
# from collections import deque
#
# present = {
#     150: "Doll",
#     250: "Wooden train",
#     300: "Teddy bear",
#     400: "Bicycle",
# }
# santa_present = {
#     "Doll": 0,
#     "Wooden train": 0,
#     "Teddy bear": 0,
#     "Bicycle": 0,
# }
# boxes = [int(x) for x in input().split()]
# magic = deque([int(x) for x in input().split()])
# the_presents_crafted = False
#
# while boxes and magic:
#     current_box = boxes.pop()
#     current_magic = magic.popleft()
#
#     if current_box > 0 and current_magic > 0:
#         result = current_magic * current_box
#         if result in present:
#
#             santa_present[present[result]] += 1
#             if (santa_present["Doll"] > 0 and santa_present["Wooden train"] > 0) or santa_present["Teddy bear"] > 0 and \
#                     santa_present["Bicycle"] > 0:
#                 the_presents_crafted = True
#
#         else:
#             boxes.append(current_box + 15)
#
#     elif current_box < 0 or current_magic < 0:
#         result = current_magic + current_box
#         boxes.append(result)
#
#     elif current_box == 0 or current_magic == 0 or (current_box == 0 and current_magic == 0):
#         if current_box == 0:
#             magic.appendleft(current_magic)
#         elif current_magic == 0:
#             boxes.append(current_box)
#         elif current_box == 0 and current_magic == 0:
#             continue
#
# if the_presents_crafted:
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
# if boxes:
#     print(f"Materials left: {', '.join([str(x) for x in boxes[::-1]])}")
# if magic:
#     print(f"Magic left: {', '.join([str(x) for x in magic])}")
# for key, value in sorted(santa_present.items()):
#     if value > 0:
#         print(f"{key}: {value}")
