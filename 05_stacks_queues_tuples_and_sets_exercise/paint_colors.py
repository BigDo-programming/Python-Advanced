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
collected_colors = set()
while text:
    first_word = text.popleft()
    last_word = text.pop() if text else ""
    word = first_word + last_word

    if word in main_colors or word in secondary_colors:
        collected_colors.add(word)
        continue

    word = last_word + first_word
    if word in main_colors or word in secondary_colors:
        collected_colors.add(word)
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
    'purple': ['red'  'blue'],
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
# ima greshka!!!