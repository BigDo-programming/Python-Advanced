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

present = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}
santa_present = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0,
}
boxes = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

while boxes and magic:
    current_box = boxes.pop()
    current_magic = magic.popleft()
    result = current_magic * current_box

    if current_box == 0 and current_magic == 0:
        continue

    if current_box == 0:
        magic.appendleft(current_magic)
        continue

    if current_magic == 0:
        boxes.append(current_box)
        continue

    if result < 0:
        boxes.append(current_magic + current_box)

    elif result in present:
        new_present = present[result]

        if new_present in santa_present:
            santa_present[new_present] += 1
        else:
            santa_present[new_present] = 1

    else:
        boxes.append(current_box + 15)

if (santa_present["Doll"] > 0 and santa_present["Wooden train"] > 0) or santa_present["Teddy bear"] > 0 and \
        santa_present["Bicycle"] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes:
    print(f"Materials left: {', '.join([str(x) for x in boxes[::-1]])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")
for key, value in sorted(santa_present.items()):
    if value > 0:
        print(f"{key}: {value}")

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
