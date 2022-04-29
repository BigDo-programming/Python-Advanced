import sys
from io import StringIO
from pprint import pprint

input1 = """5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22"""

input2 = """-15, -8, 0, -16, 0, -22
10, 5"""

input3 = """"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)
# from collections import deque
#
# firework = {
#     "Palm Fireworks": 0,
#     "Willow Fireworks": 0,
#     "Crossette Fireworks": 0,
#
# }
# firework_effects = deque([int(x) for x in input().split(", ")])
# firework_effects = deque([x for x in firework_effects if x > 0])
# explosive_powers = [int(x) for x in input().split(", ")]
# explosive_powers = [x for x in explosive_powers if x > 0]
#
# while firework_effects and explosive_powers:
#     if firework["Palm Fireworks"] >= 3 and firework["Willow Fireworks"] >= 3 and firework["Crossette Fireworks"] >= 3:
#         break
#
#     firework_effect = firework_effects.popleft()
#     explosive_power = explosive_powers.pop()
#     current_sum = firework_effect + explosive_power
#
#     if current_sum % 3 == 0 and current_sum % 5 == 0:
#         firework["Crossette Fireworks"] += 1
#
#     elif current_sum % 3 == 0:
#         firework["Palm Fireworks"] += 1
#
#     elif current_sum % 5 == 0:
#         firework["Willow Fireworks"] += 1
#
#     else:
#         if firework_effect > 1:
#             firework_effects.append(firework_effect - 1)
#         explosive_powers.append(explosive_power)
#
# if firework["Palm Fireworks"] >= 3 and firework["Willow Fireworks"] >= 3 and firework["Crossette Fireworks"] >= 3:
#     print("Congrats! You made the perfect firework show!")
# else:
#     print("Sorry. You can't make the perfect firework show.")
# if firework_effects:
#     print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")
# if explosive_powers:
#     print(f"Explosive Power left: {', '.join([str(x) for x in explosive_powers])}")
# for key, value in firework.items():
#     print(f"{key}: {value}")




from collections import deque

firework = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,

}
firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]
effect = 0
power = 0
while firework_effects and explosive_power:
    if firework["Palm Fireworks"] >= 3 and firework["Willow Fireworks"] >= 3 and firework["Crossette Fireworks"] >= 3:
        break

    if firework_effects:
        effect = firework_effects.popleft()
        if effect <= 0:
            continue
    else:
        break
    if explosive_power:
        power = explosive_power.pop()
        if power <= 0:
            firework_effects.appendleft(effect)
            continue
    else:
        break
    mix = effect + power
    if mix % 3 == 0 and not mix % 5 == 0:
        firework["Palm Fireworks"] += 1
    elif not mix % 3 == 0 and mix % 5 == 0:
        firework["Willow Fireworks"] += 1
    elif mix % 3 == 0 and mix % 5 == 0:
        firework["Crossette Fireworks"] += 1
    else:
        firework_effects.append(effect - 1)
        explosive_power.append(power)


if firework["Palm Fireworks"] >= 3 and firework["Willow Fireworks"] >= 3 and firework["Crossette Fireworks"] >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")
for key,value in firework.items():
    print(f"{key}: {value}")

