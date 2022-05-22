ll = [1, 7, 6, -1, 10, 8, -1, 12, 4, -7, 5, 2, 13, 3, 9, 14, 11]
target = 8
targets = set()
values_map = {}

for value in ll:
    if value in targets:
        p1 = value
        p2 = values_map[value]
        print(f"{p1} + {p2} = {target}")
    else:
        targets.add(target - value)
        values_map[target - value] = value
