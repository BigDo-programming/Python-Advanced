def list_manipulator(nums, add_or_remove, beginning_or_end, *args):
    new_num = [x for x in args]

    if add_or_remove == 'add':
        if beginning_or_end == "beginning":
            new_num.extend(nums)
            nums = new_num
            return nums

        elif beginning_or_end == "end":
            nums.extend(new_num)
            return nums

    elif add_or_remove == 'remove':
        if beginning_or_end == "beginning":
            if not new_num:
                if nums:
                    nums.pop(0)
                    return nums
            else:
                for i in range(*new_num):
                    nums.pop(0)
                return nums

        elif beginning_or_end == "end":
            if not new_num:
                if nums:
                    nums.pop()
                    return nums
            else:
                for i in range(*new_num):
                    nums.pop()
                return nums


# def list_manipulator(list_, command1, command2, *args):
#     if command1 == "add":
#         if command2 == "beginning":
#             for i in args[::-1]:
#                 list_.insert(0, i)
#             return list_
#         else:
#             for i in args:
#                 list_.append(i)
#             return list_
#     if command1 == "remove":
#         if command2 == "beginning":
#             if args:
#                 n = int(*args)
#                 for i in range(n):
#                     list_.pop(0)
#                 return list_
#             else:
#                 list_.pop(0)
#                 return list_
#         else:
#             if args:
#                 n = int(*args)
#                 for i in range(n):
#                     list_.pop()
#                 return list_
#             else:
#                 list_.pop()
#                 return list_
#
#
#


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
