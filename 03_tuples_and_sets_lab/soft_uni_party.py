import sys
from io import StringIO

input1 = """5
7IK9Yo0h
9NoBUajQ
Ce8vwPmE
SVQXQCbc
tSzE5t0p
9NoBUajQ
Ce8vwPmE
SVQXQCbc
END"""

input2 = """6
m8rfQBvl
fc1oZCE0
UgffRkOn
7ugX7bm0
9CQBGUeJ
2FQZT3uC
2FQZT3uC
9CQBGUeJ
fc1oZCE0
END"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)


n = int(input())
guess_list = {input() for _ in range(n)}
is_coming = set()
command = input()
while not command == "END":
    is_coming.add(command)
    command = input()

print(len(guess_list.difference(is_coming)))
for i in sorted(guess_list.difference(is_coming)):
    print(i)




# n = int(input())
# guess_list = {input() for _ in range(n)}
#
# while True:
#     command = input()
#     if command == 'END':
#         break
#     guess_list.remove(command)
#
# def is_vip(guess):
#     return guess[0].isdigit()
#     pass
#
# vip_guests = sorted([g for g in guess_list if is_vip(g)])
# regular_guests = sorted([g for g in guess_list if not is_vip(g)])
#
# print(len(guess_list))
# [print(g) for g in vip_guests]
# [print(g) for g in regular_guests]