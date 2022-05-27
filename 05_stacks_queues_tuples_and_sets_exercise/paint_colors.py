import sys
from io import StringIO

input1 = """d yel blu e low redd"""

input2 = """r ue nge ora bl ed"""

input3 = """re ple blu pop e pur d"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from collections import deque

needed_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

colors = ["red", "yellow", "blue", "orange", "purple", "green"]

main = ["red", "yellow", "blue"]
main_colors = []
secondary = ["orange", "purple", "green"]
secondary_colors = []
original_list = []

string = deque(input().split())
while string:

    first = string.popleft()
    last = string.pop() if string else ""

    if first + last in colors:
        original_list.append(first + last)

        if first + last in main:
            main_colors.append(first + last)

        else:
            secondary_colors.append(first + last)

    elif last + first in colors:
        original_list.append(last + first)

        if last + first in main:
            main_colors.append(last + first)
        else:
            secondary_colors.append(last + first)

    else:
        middle = len(string) // 2
        if len(string) == 0:
            break

        string.insert(middle, first[:-1] + last[: -1])


    # elif len(string) == 1:
    #     first = string.pop()
    #
    #     if first in colors:
    #         original_list.append(first)
    #
    #         if first in main:
    #             main_colors.append(first)
    #         else:
    #             secondary_colors.append(first)

for i in secondary_colors:
    one, two = [x for x in needed_colors[i]]
    if one not in main_colors or two not in main_colors or one not in main_colors and two not in main_colors:
        original_list.remove(i)

print(original_list)

# ToDo 60/100











# text = deque(input().split())
#
# main_colors = {"red", "yellow", "blue"}
# secondary_colors = {"orange", "purple", "green"}
# collected_colors = []
# while text:
#     first_word = text.popleft()
#     last_word = text.pop() if text else ""
#     word = first_word + last_word
#
#     if word in main_colors or word in secondary_colors:
#         collected_colors.append(word)
#         continue
#
#     word = last_word + first_word
#     if word in main_colors or word in secondary_colors:
#         collected_colors.append(word)
#         continue
#
#     first_word = first_word[:-1]
#     last_word = last_word[:-1]
#     if first_word:
#         text.insert(len(text) // 2, first_word)
#     if last_word:
#         text.insert(len(text) // 2, last_word)
#
# result = []
# required_colors = {
#     'orange': ['red', 'yellow'],
#     'purple': ['red' , 'blue'],
#     'green': ['yellow', 'blue'],
# }
# for color in collected_colors:
#     if color in main_colors:
#         result.append(color)
#     else:
#         is_valid = True
#         for required_color in required_colors[color]:
#             if required_color not in collected_colors:
#                 is_valid = False
#                 break
#         if is_valid:
#             result.append(color)
# print(result)
