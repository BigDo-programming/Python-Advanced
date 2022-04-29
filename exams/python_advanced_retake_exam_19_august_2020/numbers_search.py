def numbers_searching(*args):
    duplicate_number = {}
    duplicate = []
    for j in args:
        if j not in duplicate_number:
            duplicate_number[j] = 1
        else:
            duplicate_number[j] += 1
    for key, value in duplicate_number.items():
        if value > 1:
            duplicate.append(key)

    my_nums = set(args)

    my_min = min(args)
    my_max = max(args)
    my_number = 0
    for i in range(my_min, my_max):
        if i not in my_nums:
            my_number = i
    return [my_number, sorted(duplicate)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
