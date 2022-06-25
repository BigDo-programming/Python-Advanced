import sys
from io import StringIO

input1 = """o e a o e a i
p r s x r"""

input2 = """a a a
x r l t p p"""

input3 = """u a o i u y o e
p m t l"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)
from collections import deque

vowels = deque(input().split())
consonants = input().split()
found_flower = False
flowers_dict = {
    "rose": [],
    "tulip": [],
    "lotus": [],
    "daffodil": []
}
while vowels and consonants:
    if found_flower:
        break
    if not vowels:
        break
    if not consonants:
        break
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for key, value in flowers_dict.items():
        if found_flower:
            break
        for i in key:

            if vowel == i and i not in flowers_dict[key]:
                ch_count = key.count(i)
                for _ in range(ch_count):
                    flowers_dict[key].append(vowel)

            if consonant == i and i not in flowers_dict[key]:
                ch_count = key.count(i)
                for _ in range(ch_count):
                    flowers_dict[key].append(consonant)

            if sorted(key) == sorted(value):
                print(f"Word found: {key}")
                found_flower = True
                break

if not found_flower:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

# def check(ch, flowers):
#     for i in range(len(flowers)):
#         for j in flowers[i]:
#             if ch == j:
#                 flowers[i] = flowers[i].replace(ch, "*")
#
#     return flowers
#
#
# vowels = deque(input().split())
# consonants = input().split()
#
# finish = set()
# flowers = ["rose", "tulip", "lotus", "daffodil"]
# flowers_star = ["****", "*****", "*****", "********"]
# flowers_copy = ["rose", "tulip", "lotus", "daffodil"]
#
# while vowels or consonants:
#     if finish:
#         break
#     if not vowels:
#         break
#     if not consonants:
#         break
#     vowel = vowels.popleft()
#     flowers = check(vowel, flowers)
#     consonant = consonants.pop()
#     flowers = check(consonant, flowers)
#     for i in range(len(flowers)):
#         if flowers[i] == flowers_star[i]:
#             finish.add(flowers_copy[i])
#             break
#
# if finish:
#     print(f"Word found: {''.join(finish)}")
# else:
#     print(f"Cannot find any word!")
# if vowels:
#     print(f"Vowels left: {' '.join(vowels)}")
# if consonants:
#     print(f"Consonants left: {' '.join(consonants)}")
