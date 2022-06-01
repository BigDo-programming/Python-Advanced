def even_odd_filter(**kwargs):

    for key, value in kwargs.items():
        for i in range(len(value)):
            nums = value.pop(0)

            if key == "even":
                if nums % 2 == 1:
                    continue

                kwargs[key].append(nums)

            if key == "odd":
                if nums % 2 == 0:
                    continue

                kwargs[key].append(nums)
    return kwargs



# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
