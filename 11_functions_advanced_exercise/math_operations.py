from collections import deque


def math_operations(*args, **kwargs):
    nums = deque(args)
    while nums:
        kwargs["a"] += nums.popleft()

        if not nums:
            break

        kwargs["s"] -= nums.popleft()

        if not nums:
            break
        if not nums[0] == 0:
            kwargs["d"] /= nums.popleft()
        else:
            nums.popleft()

        if not nums:
            break
        kwargs["m"] *= nums.popleft()

    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
