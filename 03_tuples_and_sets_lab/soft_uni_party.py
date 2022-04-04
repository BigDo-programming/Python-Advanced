from cgitb import reset
from distutils import command
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

sys.stdin = StringIO(input1)

n = int(input())
guess_list = {input() for _ in range(n)}

while True:
    command = input()
    if command == 'END':
        break
    guess_list.remove(command)

def is_vip(guess):
    return guess[0].isdigit()
    pass

vip_guests = sorted([g for g in guess_list if is_vip(g)])
regular_guests = sorted([g for g in guess_list if not is_vip(g)])

print(len(guess_list))
[print(g) for g in vip_guests]
[print(g) for g in regular_guests]