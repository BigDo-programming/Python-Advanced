import sys

from io import StringIO

input1 = """d yel blu e low redd"""

input2 = """r ue nge ora bl ed"""

input3 = """re ple blu pop e pur d"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from collections import deque

text = deque(input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}
collected_colors = []
while text:
    first_word = text.popleft()
    last_word = text.pop() if text else ""
    word = first_word + last_word

    if word in main_colors or word in secondary_colors:
        collected_colors.append(word)
        continue

    word = last_word + first_word
    if word in main_colors or word in secondary_colors:
        collected_colors.append(word)
        continue

    first_word = first_word[:-1]
    last_word = last_word[:-1]
    if first_word:
        text.insert(len(text) // 2, first_word)
    if last_word:
        text.insert(len(text) // 2, last_word)

result = []
required_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue'],
}
for color in collected_colors:
    if color in main_colors:
        result.append(color)
    else:
        is_valid = True
        for required_color in required_colors[color]:
            if required_color not in collected_colors:
                is_valid = False
                break
        if is_valid:
            result.append(color)
print(result)


# from collections import deque
#
# needed_colors = {
#     "orange": ["red", "yellow"],
#     "purple": ["red", "blue"],
#     "green": ["yellow", "blue"]
# }
#
# main = ["red", "yellow", "blue"]
# secondary = ["orange", "purple", "green"]
#
#
# original_list = []
#
# string = deque(input().split())
# while string:
#
#     first = string.popleft()
#     last = string.pop() if string else ""
#
#     if first + last in main or first + last in secondary:
#         original_list.append(first + last)
#         continue
#
#     if last + first in main or last + first in secondary:
#         original_list.append(last + first)
#         continue
#
#     first = first[:-1]
#     last = last[:-1]
#
#     if first:
#         string.insert(len(string)//2, first)
#     if last:
#         string.insert(len(string)//2, last)
#
#
# result = []
# for color in original_list:
#     if color not in secondary:
#         result.append(color)
#     else:
#
#         color1,color2 = [x for x in needed_colors[color]]
#         if color1 in original_list and color2 in original_list:
#             result.append(color)
#
#
# print(result)