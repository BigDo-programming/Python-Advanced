def even_odd(*args):
    even_or_odd = args[-1]
    if_even_else_odd = 0 if even_or_odd == "even" else 1

    return [x for x in args[: -1] if x % 2 == if_even_else_odd]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

# def even_odd(*args):
#     odd = []
#     even = []
#     for i in args[:-1]:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#
#     if args[-1] == "odd":
#         return odd
#     else:
#         return even
#
#
#
# # print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


# def even_odd(*args):
#     parity = 0 if args[-1] == "even" else 1
#     return [x for x in args[:-1] if x % 2 == parity]
