from collections import deque


def best_list_pureness(list_, n):
    my_numbers = deque(list_)
    best_list_ = my_numbers.copy()
    number_sum = 0
    pureness = []

    for i in range(n + 1):
        for j in range(len(my_numbers)):
            number_sum += j * best_list_.popleft()
        pureness.append((number_sum, i))
        number_sum = 0
        best_list_ = my_numbers.copy()
        for _ in range(i + 1):
            best_list_.appendleft(best_list_.pop())
    max_num = 0
    position = 0
    for nums in pureness:
        if nums[0] > max_num:
            max_num = nums[0]
            position = nums[1]

    return f"Best pureness {max_num} after {position} rotations"



# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)

# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)
#
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
