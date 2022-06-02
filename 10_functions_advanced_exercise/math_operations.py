from collections import deque


def math_operations(*args, **kwargs):
    nums = deque(args)
    count = 0
    while nums:
        num = nums.popleft()
        count += 1
        if count > 4:
            count = (count // 4)

        if count == 1:
            kwargs['a'] += num

        elif count == 2:
            kwargs['s'] -= num

        elif count == 3:
            if not num == 0:
                kwargs['d'] /= num

        elif count == 4:
            kwargs['m'] *= num

    return '\n'.join([f"{key}: {value:.1f}" for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x))])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# print(math_operations(6.0, a=0, s=0, d=5, m=0))

# from collections import deque
#
#
# def math_operations(*args, **kwargs):
#     nums = deque(args)
#     while nums:
#         kwargs["a"] += nums.popleft()
#
#         if not nums:
#             break
#
#         kwargs["s"] -= nums.popleft()
#
#         if not nums:
#             break
#         if not nums[0] == 0:
#             kwargs["d"] /= nums.popleft()
#         else:
#             nums.popleft()
#
#         if not nums:
#             break
#         kwargs["m"] *= nums.popleft()
#
#     return kwargs


# def math_operations(*args, **kwargs):
#     count = 0
#     for j in range(len(args) // 2 + 1):
#         for i in range(count, len(args), 4):
#
#             if count == 0 and not args[i] is None:
#                 kwargs['a'] += args[i]
#
#             if count == 1 and not args[i] is None:
#                 kwargs['s'] -= args[i]
#
#             if count == 2 and not args[i] is None:
#                 if not args[i] == 0:
#                     kwargs['d'] /= args[i]
#
#             if count == 3 and not args[i] is None:
#                 kwargs['m'] *= args[i]
#
#         count += 1
#     return '\n'.join([f"{key}: {value:.1f}" for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x))])
